#   Exception Handling

names_tuple = 'Rod', 'Jane', 'Freddy'
# TRY Block
# Try block attempts to run the code
try:
    print("######## TRY ########")
    print("The TRY block attempts to run")
    print(f"Original Tuple: {names_tuple}")
    names_sorted_as_a_list = sorted(names_tuple)
#   sorted() function returns a list in ascending order (alphabetical order for strings)
#   therefore, tuple is transformed into a list.
    print(names_sorted_as_a_list)
    names_sorted_as_a_list.append("Bungle")
#   we are able to append (add) the object "Bungle" onto the list as lists are mutable.
#   'Bungle' is added to the end of the list (not in alphabetical order) since .append() method was used.
    print("Added Bungle:",names_sorted_as_a_list)
    print("Attempt to manipulate the tuple...")
    names_tuple[0] = 'Zippy'
#   when this line is commented out, the except blocks do not run as all the code in the try block is able to be run.
#   This command does not work as variable 'names_tuple' is a tuple and tuples are immutable.
#   Therefore, cannot be appended.
#     if names_tuple:
#     print(names_tuple)
    print("Is this code reached?")
#    This code isn't reached when 'names_tuple[0] = 'Zippy'' is uncommented because this is where the code runs into an error and goes to the except blocks
except FileNotFoundError as error:
#   Exception blocks only run if the defined error occurs.
#   If there is an error identified in the TRY block, the script will run through each except block in order.
#   FileNotFoundError runs when a file or directory is requested but does not exist.
#   This error does not apply to this script as no file or directory is requested, therefore, this except block does not run.
    print("######## EXCEPT: FileNotFoundError ########")
    print("The EXCEPT / CATCH block only runs if this error happens")
    print(f"The following file can not be found: {error.filename}. Please try another file")
#   .filename class attribute --> file that doesn't exist.
except TypeError as error:
#   TypeError is raised when an operating function is applied to an object of an inappropriate type.
#   In this case, code attempted to replace string object in position 0 of tuple, however, tuples are immutable, therefore, operation could not be completed.
#   Because this error occurs, TypeError exception block runs and prints the subsequent messages.
    print("######## EXCEPT: TypeError ########")
    print("Oh dear, that is not allowed on that type")
    print(error)
except Exception as error:
#   Exception detects all built-in non-exiting exceptions that are derived from this class.
#   This block will identify errors that are not mentioned in previous exception blocks.
    print("######## EXCEPT: Exception ########")
    print("Generic catch-all except / catch block")
    print(error)
finally:
    # Always close file handle after use.
    print("The FINALLY block ALWAYS runs")
    print("The finally block is used to tidy up")
    if names_tuple:
        names_tuple = None
#   The above if line asks if names_tuple holds a value (is not empty).
#   Because it does, the code underneath runs.
#   = None assigns no value to the variable.
print("After exception handling is finished... the program can continue")