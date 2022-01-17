from setuptools import setup
setup(name='dashboard',
      description='Displays a dashboard and calculates the moving 2 day average',
      author='Michael Hopkins',
      author_email='mbh4480@rit.edu',
      python_requires='>=3.7.1',
      install_requires=['pandas>=1.3.5', 'plotly>=4.8', 'dash>=2.0']
)