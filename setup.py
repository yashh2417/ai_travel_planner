from setuptools import setup, find_packages
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_list:List[str] = []
    
    try:
        # Open and read the requirements.txt file
        with open('requirements.txt', 'r') as file:
            # Read lines from the file
            lines = file.readlines()
            # Process each line
            for line in lines:
                # Strip whitespace and newline characters
                requirement = line.strip()
                # Ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")

    
        
    return requirement_list
print(get_requirements())

setup(
    name="ai_travel_planner",
    version="0.1.0",
    description="Agentic AI Travel Agent helps you plan smart, budget-friendly trips by using real-time data on weather, events, hotels, transport, and more — all powered by AI.",
    author="Yash",
    author_email="yashh2417@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
    python_requires=">=3.10"
)

