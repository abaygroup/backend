# from django.contrib.contenttypes.models import ContentType
# from .models import OverviewProduct


# def create_overview_product(sender, instance, created, **kwargs):
#     content_type = ContentType.objects.get_for_model(instance)
#     try:
#         overview_product = OverviewProduct.objects.get(content_type=content_type, object_id=instance.id)
#     except OverviewProduct.DoesNotExist:
#         overview_product = OverviewProduct(content_type=content_type, object_id=instance.id)

#     overview_product.save()