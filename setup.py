from setuptools import setup
setup(
    name="agent-hub",
    version="0.1.0",
    py_modules=["agent_hub"],
    entry_points={"console_scripts": ["agent-hub=agent_hub:cli"]},
    install_requires=["click>=8.0", "requests>=2.28", "fastapi>=0.104"],
    python_requires=">=3.9",
)
