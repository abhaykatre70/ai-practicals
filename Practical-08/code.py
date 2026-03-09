# --- ISA Relationships (inheritance hierarchy) ---
isa = {
    "bird": "animal",
    "dog": "animal",
    "sparrow": "bird"
}

# --- CAN-DO Relationships (abilities) ---
can_do = {
    "bird": ["fly"],
    "dog": ["bark"]
}

# --- HAS-PROPERTY Relationships ---
has_property = {
    "animal": ["cells"]
}


# Helper: get the direct superclass of a concept
def get_superclass(concept):
    return isa.get(concept, None)


# Query: does 'concept' have 'property_name'? (with inheritance)
def inherits_property(concept, property_name):
    if concept in has_property and property_name in has_property[concept]:
        return True
    parent = get_superclass(concept)
    if parent:
        return inherits_property(parent, property_name)
    return False


# Query: can 'concept' perform 'ability'? (with inheritance)
def inherits_ability(concept, ability):
    if concept in can_do and ability in can_do[concept]:
        return True
    parent = get_superclass(concept)
    if parent:
        return inherits_ability(parent, ability)
    return False


# --- Queries ---
print("Does dog have cells?    ->", inherits_property("dog", "cells"))
print("Does sparrow have cells? ->", inherits_property("sparrow", "cells"))
print("Can sparrow fly?        ->", inherits_ability("sparrow", "fly"))
print("Can dog fly?            ->", inherits_ability("dog", "fly"))
