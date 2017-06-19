import math,random,operator
from collections import Container
import abc


class Property:
    def __init__(self,squareFeet="",beds="",baths="",**kwargs):
        super().__init__(**kwargs)
        self.squareFeet=squareFeet
        self.numBedrooms=beds
        self.numBaths=baths

    def display(self):
        print("Property Details")
        print("=================")
        print("square footage: {}".format(self.squareFeet))
        print("bedrooms: {}".format(self.numBedrooms))
        print("Baths:  {}".format(self.numBaths))
        print()

    def prompt_init():
        return dict(squareFeet=input("Enter the square feet: "),
                    beds=input("Enter number of bedrooms"),
                    baths=input("Enter number of baths"))

    prompt_init=staticmethod(prompt_init)

class Apartment(Property):
    valid_laundries=("coin","ensuite","none")
    valid_balconies=("yes","no","solarium")

    def __init__(self,balcony="",laundry="",**kwargs):
        super().__init__(**kwargs)
        self.balcony=balcony
        self.laundry=laundry

    def display(self):
        super().display()
        print("APARTMENT DETALS")
        print("Laundry: %s" % (self.laundry))
        print("has balcony: %s" % (self.balcony))

    def prompt_init():
        parent_init=Property.prompt_init()
        laundry=get_valid_input("What laundry",Apartment.valid_laundries)
        balcony=get_valid_input("What balcony",Apartment.valid_balconies)

        parent_init.update({
        "laundry":laundry,
        "balcony":balcony
        })
        return parent_init
    prompt_init=staticmethod(prompt_init)

class House(Property):
    valid_garage=("attached","detached","none")
    valid_fenced=("yes","no")

    def __init__(self,stories='',garage="",fenced="",**kwargs):
        super().__init__(**kwargs)
        self.stories=stories
        self.garage=garage
        self.fenced=fenced

    def display(self):
        super().display()
        print("HOUSE DETAILS")
        print("# of stories: {}".format(self.stories))
        print("Garage: {}".format(self.garage))
        print("Fenced yard: {}".format(self.fenced))

    def prompt_init():
        parent_init=Property.prompt_init()
        fenced=get_valid_input("Type of fence",House.valid_fenced)
        garage=get_valid_input("Type of garage",House.valid_garage)
        stories=input("How many stories")

        parent_init.update({
        "garage":garage,
        "fenced":fenced,
        "stories":stories
        })
        return parent_init
    prompt_init=staticmethod(prompt_init)

class Purchase:
    def __init__(self,price="",taxes="",**kwargs):
        super().__init__(**kwargs)
        self.price=price
        self.taxes=taxes

    def display(self):
        super().display()
        print("Purchase Details")
        print("Selling price: {}".format(self.price))
        print("Estimated taxes: {}".format(self.taxes))


    def prompt_init():
        return dict(
        price=input("What is selling price"),
        taxes=input("What are the estimated taxes")
        )


class Rental:
    def __init__(self,furnished="",utilities="",rent="",**kwargs):
        super().__init__(**kwargs)
        self.furnished=furnished
        self.rent=rent
        self.utlities=utilities

    def display(self):
        super().display()
        print("Rental Details")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {} ".format(self.utlities))
        print("furnished: {}".format(self.furnished))

    def prompt_init():
        return dict(
            rent=input('What is monthly rent'),
            utilities=input("What are estimated utilities"),
            furnished=get_valid_input("Is property furnished",("yes","no")))

    prompt_init=staticmethod(prompt_init)

class HouseRental(Rental,House):
    def prompt_init():
        init=House.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init=staticmethod(prompt_init)

class ApartmentRental(Rental,Apartment):
    def prompt_init():
        init=Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init=staticmethod(prompt_init)

class HousePurchase(Purchase,House):
    def prompt_init():
        init=House.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init=staticmethod(prompt_init)

class ApartmentPurchase(Purchase,Apartment):
    def prompt_init():
        init=Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init=staticmethod(prompt_init)

class Agent:
    type_map={
    ("house","rental"):HouseRental,
    ("house","purchase"):HousePurchase,
    ("apartment","rental"):ApartmentRental,
    ("apartment","purchase"):ApartmentPurchase
    }

    def __init__(self):
        self.property_list=[]

    def display_properties(self):
        for property in self.property_list:
            property.display()

    def add_property(self):
        property_type=get_valid_input(
        "What type of property? ",
        ("house","apartment")).lower()
        payment_type=get_valid_input(
        "What payment type? ",
        ("purchase","rental")).lower()

        PropertyClass=self.type_map[(property_type,
        payment_type)]
        init_args=PropertyClass.prompt_init()
        print("Here")
        self.property_list.append(PropertyClass(**init_args))



def get_valid_input(input_string,valid_options):
    input_string+=" ({}) ".format(", ".join(valid_options))
    response=input(input_string)
    while response.lower()  not in valid_options:
        response=input(input_string)
    return response

agent=Agent()
agent.add_property()
agent.display_properties()
