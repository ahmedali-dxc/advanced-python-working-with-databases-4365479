from sqlalchemy import create_engine, Column, Integer, String, Numeric, select, func
from sqlalchemy.orm import registry, Session

engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/red30', echo=True)

mapper_registry = registry()

Base = mapper_registry.generate_base()

class Sale(Base):
    __tablename__ = 'Sales'
    order_num = Column(Integer, primary_key=True)
    cust_name = Column(String(length=255))
    prod_name = Column(String(length=255))
    prod_number = Column(String(length=255))
    quantity = Column(Integer)
    price = Column(Numeric)
    discount = Column(Numeric)
    order_total = Column(Numeric)

    def __repr__(self):
        return ("<Sale(order_num='{0}', cust_name='{1}', prod_name='{2}', prod_number='{3}', quantity='{4}', price='{5}', discount='{6}', order_total='{7}')>"
        .format(self.order_num, self.cust_name, self.prod_name, self.prod_number, self.quantity, self.price, self.discount, self.order_total))

Base.metadata.create_all(engine)

with Session(engine, future=True) as session:
    sale1 = Sale(order_num=1100935, cust_name='Spencer Educator', prod_number='DK204', prod_name='BY0D-300', quantity=2,
                 price=89, discount=0, order_total=178)
    sale2 = Sale(order_num=1100948, cust_name='Ewan Ladd', prod_number='TV810', prod_name='Understanding Automation',
                 quantity=1, price=44.95, discount=0, order_total=44.95)
    sale3 = Sale(order_num=1100963, cust_name='Stehr Group', prod_number='DS301', prod_name='AD-SA702 Drone',
                 quantity=3, price=399, discount=1, order_total=1077)
    sale4 = Sale(order_num=1100971, cust_name='Hettinger and Sons', prod_number='DS306', prod_name='AD-SA702 Drone',
                 quantity=12, price=250, discount=5, order_total=1500)
    sale5 = Sale(order_num=1100998, cust_name="Luz O'Donohue", prod_number='TV809', prod_name='Understanding 3D Printing',
                 quantity=1, price=42.99, discount=0, order_total=42.99)
    sales = [sale1, sale2, sale3, sale4, sale5]

    session.bulk_save_objects(sales)
    session.flush()
    session.commit()

    # max order total
    max_query = select(func.max(Sale.order_total))
    max_order = session.execute(max_query).scalar()
    print(max_order)

    # sorted by order total desc
    result_query = select(Sale).order_by(Sale.order_total.desc())
    result_by_total_order_desc = session.execute(result_query).scalar()
    print(result_by_total_order_desc)
