from dukan.models import Seller
from django.core import serializers


class SellerModel:

    def __init__(self):

        self.seller = Seller.objects

    def get_seller_by_id(self, id):

        sellerobject = self.seller.get(id=id)
        serialized_obj = serializers.serialize('json', [ sellerobject, ])
        return serialized_obj

    def filter_sellers_by_name(self, args):
        
        sellerobject = self.seller.filter( brand_name = args)
        sellerobject = list(sellerobject.values())

        return sellerobject