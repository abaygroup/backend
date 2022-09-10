from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


class UserManager(BaseUserManager):
    def create_user(self, username, email, full_name, password=None):
        if not username:
            raise ValueError(_('There must be a user name'))
        if not email:
            raise ValueError(_('The user must have an email address'))
        if not full_name:
            raise ValueError(_('There must be a name'))

        user = self.model(username=username.lower(), full_name=full_name, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, full_name, password=None):
        user = self.create_user(username, email, full_name, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


# User model
# ========================================================================
class User(AbstractBaseUser, PermissionsMixin):

    GENDER_CHOICES = (
        ('NOT_DEFINED', _('Not defined')),
        ('MALE', _('Male')),
        ('FAMALE', _('Famale')),
    )

    username = models.CharField(verbose_name=_('username'), max_length=32, unique=True)
    email = models.EmailField(verbose_name=_('email address'), max_length=64, unique=True)
    full_name = models.CharField(verbose_name=_('full name'), max_length=64)
    gender = models.CharField(verbose_name=_('gender'), max_length=64, choices=GENDER_CHOICES, default=GENDER_CHOICES[0][1])
    phone = models.PositiveIntegerField(verbose_name=_('phone'), null=True, blank=True)
    birthday = models.DateField(verbose_name=_('birthday'), blank=True, null=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'full_name', ]

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username


    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
# ========================================================================


# User payment history
# ========================================================================
class PaymentHistory(models.Model):
    user = models.OneToOneField(User, verbose_name=_('User'), on_delete=models.CASCADE, default=None)
    payment_for = models.ForeignKey('Membership', on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(verbose_name=_('Price'), max_digits=10, decimal_places=2, default=0)
    payment_date = models.DateField(verbose_name=_('Payment date'), auto_now_add=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _('Payment history')
        verbose_name_plural = _('Payment histories')


# Membership (Account plan)
# ========================================================================
class Membership(models.Model):

    MEMBERSHIP_CHOICES = (
        ('FREE', _('Free')),
        ('PREMIUM', _('Premium')),
        ('PREMIUM_FOR_DUO', _('Premium for duo')),
        ('PREMIUM_FOR_GROUP', _('Premium for group')),
        ('PREMIUM_FOR_STUDENTS', _('Premium for students')),
    )

    slug = models.SlugField(verbose_name=_('Slug'), null=True, blank=True)
    membership_type = models.CharField(
        verbose_name=_('Membership type'),
        choices=MEMBERSHIP_CHOICES,
        max_length=60,
        default=MEMBERSHIP_CHOICES[0][1])
    price = models.DecimalField(verbose_name=_('Price'), max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.membership_type

    class Meta:
        verbose_name = _('Membership')
        verbose_name_plural = _('Memberships')


class UserMembership(models.Model):
    user = models.OneToOneField(User, related_name='user_membership', verbose_name=_('User'), on_delete=models.CASCADE)
    membership = models.ForeignKey(
        Membership,
        related_name='user_membership',
        verbose_name=_('Membership'),
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _('User membership')
        verbose_name_plural = _('User memberships')


class Subscription(models.Model):
    user_membership = models.ForeignKey(UserMembership, related_name='subscription', on_delete=models.CASCADE)
    active = models.BooleanField(verbose_name=_('Active'), default=True)

    def __str__(self):
      return self.user_membership.user.username

    class Meta:
        verbose_name = _('Subscription')
        verbose_name_plural = _('Subscriptions')

# =====================================================================================


# Profile model
# =====================================================================================
class Profile(models.Model):

    def validate_image(logotype):
        file_size = logotype.size
        megabyte_limit = 3.0
        if file_size > megabyte_limit*1024*1024:
            raise ValidationError(_("The maximum file size should be {}MB").format(str(megabyte_limit)))

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('User'))
    image = models.ImageField(verbose_name=_('Image'), validators=[validate_image], upload_to='accounts/profile/image/', blank=True, null=True, help_text=_('The maximum file size is 2MB'))
    branding = models.BooleanField(verbose_name=_('Branding'), default=False)
    about_me = models.TextField(verbose_name=_('About me'), max_length=300, blank=True, null=True)
    address = models.TextField(verbose_name=_('Address'), max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

# =====================================================================================