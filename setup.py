import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='Discrept',
    version='1.2',
    scripts=['discrept.py'],
    author="Andrew Reed",
    author_email="AndrewReed2017@icloud.com",
    description="A Language that Generates PDF / Math coding language",
    long_description=long_description,
    url="https://github.com/areed2017/DiscreptIDE",
    packages=[
        'discreptide',
        'discreptide.control',
        'discreptide.model',
        'discreptide.view',
        'discreptide.view.pdf_viewer',
        'discreptide.view.settings',
    ],
    data_files=[('styles', ['styles/document.css', 'styles/lab report.css'])],

    install_requires=[
          'weasyprint',
          'subscrept',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
 )