# Finder Package

The `finder` package is responsible for finding and extracting metadata from files in a directory tree. It includes the following modules:

- `finder.py`: Main module for the `finder` package.
- `pathfinder.py`: Provides the `PathFinder` class for finding files in a directory tree.
- `stepextractor.py`: Provides the `StepExtractor` class for extracting directory steps from file paths.
- `detailsextractor.py`: Provides the `DetailsExtractor` class for extracting detailed metadata from filenames.
- `utils.py`: Provides utility functions for file and path operations, and database interactions.

## Usage

To use the `finder` package, you can initialize the `Finder` class and call the `run` method with the desired directory and extensions.

Example usage:

```python
from finder import Finder

# Specify directory and extensions
directory = '/path/to/your/directory'
extensions = ('.mp4', '.mkv', '.avi')

# Initialize Finder object
finder = Finder()

# Run the Finder process with specified directory and extensions
finder.run(directory=directory, extensions=extensions)

Command line usage:

# Run in the terminal
```bash
python finder.py /E:/Films/Movies/History/Manhunts .mp4 .mkv .avi

```
