import peewee

data = peewee.SqliteDatabase('data.db')

class Produto(peewee.Model):
    name =  peewee.CharField()
    description = peewee.TextField()
    stock = peewee.IntegerField()
    price = peewee.FloatField()

    def to_dict():
        return {'id': self.id , 'name': self.name , 'description': self.description , 'stock': self.stock , 'price': self.price}

    class Meta:
        database = data
    

try:
    data.create_table(Produto)
except Exception as e:
    pass


