class ProductFactory(factory.Factory):
    class Meta:
        model = dict  # or your Product model

    id = factory.Sequence(lambda n: n)
    name = factory.Faker("word")
    category = factory.Faker("word")
    available = factory.Faker("boolean")
    price = factory.Faker("pyfloat", left_digits=3, right_digits=2, positive=True)
