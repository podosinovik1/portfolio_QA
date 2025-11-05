from dataclasses import dataclass
from typing import Optional, Dict, Union
from random import choice


@dataclass
class Data:
    """
    Data container for object attributes.
    
    Represents product specifications with optional fields for electronics:
    - Technical specifications (CPU, screen, capacity)
    - Product information (year, generation, color) 
    - Pricing data
    """
    year: Optional[int] = None
    price: Optional[Union[int, float]] = None
    cpu_model: Optional[str] = None
    color: Optional[str] = None
    capacity: Optional[str] = None
    screen_size: Optional[Union[int, float]] = None
    generation: Optional[str] = None

    def to_dict(self) -> Dict:
        """Convert to dictionary with proper None handling"""
        result = {}
        if self.year is not None:
            result["year"] = self.year
        if self.price is not None:
            result["price"] = self.price
        if self.cpu_model is not None:
            result["CPU model"] = self.cpu_model
        if self.color is not None:
            result["color"] = self.color
        if self.capacity is not None:
            result["capacity"] = self.capacity
        if self.screen_size is not None:
            result["screen size"] = self.screen_size
        if self.generation is not None:
            result["generation"] = self.generation
        return result


@dataclass
class Object:
    """
    Main object container with name and nested data.
    
    Represents a product entity with:
    - Product name identifier
    - Optional specifications data dictionary
    """
    name: str
    data: Data.to_dict = None

    def to_dict(self) -> Dict:
        """Convert to dictionary with data validation"""
        result = {"name": self.name}
        if self.data is not None:
            result["data"] = self.data
        return result


class TestData:
    """
    Test data generator for object API testing.
    
    Provides methods to generate valid and invalid test data
    for electronics products (laptops, phones, tablets).
    Contains predefined valid and invalid value ranges.
    """
    
    # Valid test data ranges
    VALID_YEARS = list(range(2018, 2024))
    VALID_PRICES = [499.99, 799.99, 999.99, 1299.99, 1999.99]
    VALID_CPU_MODELS = ["Intel i5", "Intel i7", "Intel i9", 
                        "Apple M1", "Apple M2", "AMD Ryzen 5", 
                        "AMD Ryzen 7"]
    VALID_COLORS = ["Space Gray", "Silver", "Gold", "Rose Gold", 
                    "Black", "Blue", "Red"]
    VALID_CAPACITIES = ["128GB", "256GB", "512GB", "1TB", "2TB"]
    VALID_SCREEN_SIZES = [13.3, 14, 15.6, 16, 17]
    VALID_GENERATIONS = ["8th", "9th", "10th", "11th", "12th", 
                         "13th", "2020", "2021", "2022", "2023"]
    
    # Product types
    PRODUCT_TYPES = {
        "laptop": ["MacBook Pro", "Dell XPS", "Lenovo ThinkPad", "HP Spectre", "Asus ZenBook"],
        "phone": ["iPhone", "Samsung Galaxy", "Google Pixel", "OnePlus"],
        "tablet": ["iPad", "Samsung Tablet", "Microsoft Surface"]
    }

    # Invalid test data
    INVALID_YEARS = [-2023, 0, 10000, 1800, "2023", True, None]
    INVALID_PRICES = [-999.99, 0, 999999.99, "expensive", True, []]
    INVALID_CPU_MODELS = ["", "X" * 100, "Invalid@CPU", 123, True]
    INVALID_COLORS = ["", "Color123", "X" * 50, 123, []]
    INVALID_CAPACITIES = ["", "128", "256MB", "Invalid", 512, True]
    INVALID_SCREEN_SIZES = [-13.3, 0, 100.5, "large", True, {}]
    INVALID_GENERATIONS = ["", "999th", "X" * 100, 13, True]
    INVALID_NAMES = ["", "X" * 1000, "Invalid@Product!", 123, True, None, []]

    @classmethod
    def random_types(cls):
        """Randomly select from available product types."""
        types = cls.PRODUCT_TYPES.keys()
        return choice(list(types))

    @classmethod
    def random_product(cls):
        """Randomly select product name from available types."""
        type_product = cls.random_types()
        product = cls.PRODUCT_TYPES[type_product]
        return choice(product)

    @classmethod
    def random_valid_data(cls):
        """Generate valid test data with complete specifications."""
        return Object(
            name=cls.random_product(),
            data=Data(
                year=choice(cls.VALID_YEARS),
                price=choice(cls.VALID_PRICES),
                cpu_model=choice(cls.VALID_CPU_MODELS),
                color=choice(cls.VALID_COLORS),
                capacity=choice(cls.VALID_CAPACITIES),
                screen_size=choice(cls.VALID_SCREEN_SIZES),
                generation=choice(cls.VALID_GENERATIONS)
            ).to_dict()
        ).to_dict()

    @classmethod
    def random_invalid_name(cls):
        """Generate object with invalid name field."""
        return Object(
            name=choice(cls.INVALID_NAMES),
            data=Data(
                year=choice(cls.VALID_YEARS),
                price=choice(cls.VALID_PRICES),
                cpu_model=choice(cls.VALID_CPU_MODELS)
            ).to_dict()
        ).to_dict()

    @classmethod
    def random_invalid_year(cls):
        """Generate object with invalid year field."""
        return Object(
            name=cls.random_product(),
            data=Data(
                year=choice(cls.INVALID_YEARS),
                price=choice(cls.VALID_PRICES),
                cpu_model=choice(cls.VALID_CPU_MODELS)
            ).to_dict()
        ).to_dict()

    @classmethod
    def random_invalid_price(cls):
        """Generate object with invalid price field."""
        return Object(
            name=cls.random_product(),
            data=Data(
                year=choice(cls.VALID_YEARS),
                price=choice(cls.INVALID_PRICES),
                cpu_model=choice(cls.VALID_CPU_MODELS)
            ).to_dict()
        ).to_dict()

    @classmethod
    def random_invalid_cpu_model(cls):
        """Generate object with invalid CPU model field."""
        return Object(
            name=cls.random_product(),
            data=Data(
                year=choice(cls.VALID_YEARS),
                price=choice(cls.VALID_PRICES),
                cpu_model=choice(cls.INVALID_CPU_MODELS)
            ).to_dict()
        ).to_dict()

    @classmethod
    def random_invalid_capacity(cls):
        """Generate object with invalid capacity field."""
        return Object(
            name=cls.random_product(),
            data=Data(
                year=choice(cls.VALID_YEARS),
                price=choice(cls.VALID_PRICES),
                capacity=choice(cls.INVALID_CAPACITIES)
            ).to_dict()
        ).to_dict()

    @classmethod
    def random_invalid_screen_size(cls):
        """Generate object with invalid screen size field."""
        return Object(
            name=cls.random_product(),
            data=Data(
                year=choice(cls.VALID_YEARS),
                price=choice(cls.VALID_PRICES),
                screen_size=choice(cls.INVALID_SCREEN_SIZES)
            ).to_dict()
        ).to_dict()

    @classmethod
    def random_mixed_invalid_data(cls):
        """Generate object with multiple invalid fields."""
        return Object(
            name=choice(cls.INVALID_NAMES),
            data=Data(
                year=choice(cls.INVALID_YEARS),
                price=choice(cls.INVALID_PRICES),
                cpu_model=choice(cls.INVALID_CPU_MODELS),
                capacity=choice(cls.INVALID_CAPACITIES),
                screen_size=choice(cls.INVALID_SCREEN_SIZES)
            ).to_dict()
        ).to_dict()


def payload(case):
    """
    Test payload generator for API testing.
    
    Args:
        case: Test case identifier string
        
    Returns:
        Dictionary with payload data for the specified test case
        
    Raises:
        ValueError: If unknown test case provided
    """
    cases = {
        "valid_data": TestData.random_valid_data,
        "invalid_name": TestData.random_invalid_name,
        "invalid_year": TestData.random_invalid_year,
        "invalid_price": TestData.random_invalid_price,
        "invalid_cpu_model": TestData.random_invalid_cpu_model,
        "invalid_capacity": TestData.random_invalid_capacity,
        "invalid_screen_size": TestData.random_invalid_screen_size,
        "mixed_invalid_data": TestData.random_mixed_invalid_data,
    }

    if case not in cases:
        raise ValueError(f"Unknown test case: {case}")
    
    data = cases[case]()
    return data

import json

print(type(json.dumps(payload("valid_data"))))
