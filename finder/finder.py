import argparse
from pathfinder import PathFinder
from stepextractor import StepExtractor
from detailsextractor import DetailsExtractor

'''
Finder class is the main class for the finder module.
It provides methods for finding files in a directory tree, 
extracting directory steps from file paths, 
and extracting file details from file paths.

The Finder (Find Extractor) class is used by the Classifier class in the classifier module to find files in a directory tree for indexing.

The Finder class is composed of the PathFinder, StepExtractor, and DetailsExtractor classes.

The PathFinder class is used to find files in a directory tree that match a specified pattern.

The StepExtractor class is used to extract directory steps from file paths by removing the root directory and filename.

The DetailsExtractor class is used to extract details from the filenames of files in the filepaths table in the classified.db database.

The Finder class provides a method for finding files in a directory tree that match a specified pattern, extracting directory steps from file paths, and extracting file details from file paths.
'''

class Finder:
    '''Initialize Finder class'''
    def __init__(self):
        pass

    def run(self, directory, extensions):
        '''Run the Finder process'''

        # Find files in directory: PathFinder
        pathfinder = PathFinder(filepath=directory)

        # Find files in directory tree
        files = pathfinder.find(path=directory, extensions=extensions)
        print("Files found and saved to database")  # Debug print

        # Extract directory steps from file paths: StepExtractor
        stepextractor = StepExtractor()

        # Extract directory steps
        stepextractor.extract()
        print("Directory steps extracted and saved to database")  # Debug print

        # Extract details from file paths: DetailsExtractor
        detailsextractor = DetailsExtractor()

        # Extract details from filenames
        detailsextractor.extract()
        print("Details extracted and saved to database") # Debug print

# Define main function
def main():
    '''Main function to run the Finder process'''

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Run the Finder process')
    parser.add_argument('directory', type=str, help='Directory to search for files')
    parser.add_argument('extensions', type=str, nargs='+', help='File extensions to search for')
    args = parser.parse_args()

    # Initialize Finder object
    finder = Finder()

    # Run the Finder process with specified directory and extensions
    finder.run(directory=args.directory, extensions=tuple(args.extensions))

# Run main function
if __name__ == "__main__":
    main()