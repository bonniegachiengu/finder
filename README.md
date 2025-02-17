# Finder Package

The `finder` package is responsible for finding and extracting metadata from files in a directory tree. It includes the following modules:

- `finder.py`: Main module for the `finder` package.
- `pathfinder.py`: Provides the `PathFinder` class for finding files in a directory tree.
- `stepextractor.py`: Provides the `StepExtractor` class for extracting directory steps from file paths.
- `detailsextractor.py`: Provides the `DetailsExtractor` class for extracting detailed metadata from filenames.
- `utils.py`: Provides utility functions for file and path operations, and database interactions.

## Usage

To use the `finder` package, you can initialize the `PathFinder`, `StepExtractor`, and `DetailsExtractor` classes to find files, extract directory steps, and extract detailed metadata, respectively.

Example usage:

```python
from finder.pathfinder import PathFinder
from finder.stepextractor import StepExtractor
from finder.detailsextractor import DetailsExtractor

# Initialize PathFinder object
pathfinder = PathFinder(filepath='path/to/directory')

# Find files in directory tree
pathfinder.find(path='path/to/directory', extensions=('.txt', '.pdf'))

# Initialize StepExtractor object
stepextractor = StepExtractor()

# Extract directory steps from file paths
stepextractor.extract()

# Initialize DetailsExtractor object
details_extractor = DetailsExtractor()

# Extract details from filenames and save to database
details_extractor.extract()
```
