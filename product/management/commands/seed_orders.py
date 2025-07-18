import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.contrib.auth import get_user_model

from account.models import Rider, Vendor
from product.models import Order, Product

User = get_user_model()


class Command(BaseCommand):
    help = "Seed 20 orders for the first user"

    def handle(self, *args, **kwargs):

        user = User.objects.get(email='mozezcharles@gmail.com')

        print(user)

        rider = Rider.objects.get(user=user)

        orders = Order.objects.all()


        status = [
            "picked_up",
            "in_transit",
            "delivered",
        ]

        for order in orders:
            random_status = random.choice(status)
            order.delivery_status = random_status
            order.rider = rider
            order.save()
            print(order.delivery_status)
        



        return
        user = User.objects.first()
        if not user:
            self.stdout.write(self.style.ERROR("❌ No user found in the database."))
            return

        vendors = list(Vendor.objects.all())
        products = list(Product.objects.filter(is_active=True))

        if not vendors or not products:
            self.stdout.write(self.style.ERROR("❌ Vendors or products are missing."))
            return

        created_orders = []

        for _ in range(20):
            vendor = random.choice(vendors)

            order = Order(
                user=user,
                vendor=vendor,
                status='pending',
                payment_status=Order.PENDING,
                delivery_status='pending',
                country='CountryX',
                state='StateY',
                city='CityZ',
                address='123 Example Street',
                location_latitude=6.5244,
                location_longitude=3.3792,
                total_amount=0.00,  # You can update later with items
            )
            created_orders.append(order)

        Order.objects.bulk_create(created_orders)

        # Re-fetch and individually save to trigger track_id generation
        for order in Order.objects.filter(user=user).order_by('-created_at')[:20]:
            order.save()

        self.stdout.write(self.style.SUCCESS("✅ Successfully created 20 orders for user: %s" % user.email))
