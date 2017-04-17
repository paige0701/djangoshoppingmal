from shopping_app.models import Product



# 이것도 하루에 한번만 view 가 올라간다던지 아이피 주소에 한번만 올라간다던지 뭐 그런식으로 할 수 잇으면 해보자
class ViewIncrease(object):

    def increaseview(self, id):

        product = Product.objects.get(id=id)
        product.views += 1
        product.save()
        return product