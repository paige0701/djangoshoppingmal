from django.http import request

from shopping_app.models import Product, Comment, User, Cart


# 이것도 하루에 한번만 view 가 올라간다던지 아이피 주소에 한번만 올라간다던지 뭐 그런식으로 할 수 잇으면 해보자
class ViewIncrease(object):

    def increaseview(self, id):

        product = Product.objects.get(id=id)
        product.views += 1
        product.save()
        return product

# Comment 관한 클라스
class CommentClass(object):

    #Comment 를 add 한다
    def addcomment(self,username,content,product):

        user = User.objects.get(id=username)
        product = Product.objects.get(id=product)
        comment = Comment(author=user, content=content, product=product)
        comment.save()
        return comment


    # Comment Edit
    def editcomment(self):
        pass

    # Comment delete
    def deletecomment(self):
        pass


class CartClass(object):

    # cart add
    def addCart(self, userid, productid, quantity):

        userid = User.objects.get(id=userid)
        productid = Product.objects.get(id=productid)

        print("111")
        cart = Cart.objects.filter(user=userid,product=productid)
        # print("222", cart)
        if cart:
            print("333")
            for x in cart:

                quantity = int(quantity)
                x.quantity += quantity
                x.save()
            return cart

        else:
            print("444")
            cart = Cart(user=userid, product=productid, quantity=quantity)
            cart.save()
            return cart


    # Cart delete
    def deleteCart(self):
        pass


    # Cart edit (quantity)
    def editCart(self, userid, productid, quantity):

        user = User.objects.get(id=userid)
        product = Product.objects.get(id=productid)
        cart = Cart.objects.filter(user=user, product=product)
        for x in cart:
            x.quantity = int(quantity)
            x.save()

        return cart