names_tuple = 'Rod', 'Jane', 'Freddy'
# the above collection is a tuple as its the content of collection is divided by the ","

# exceptional handling i s initiated by the try statement
try:
    print("######## TRY ########")
    #  print statement is run
    print("The TRY block attempts to run")
    # print statement is run

    print(f"Original Tuple: {names_tuple}")
    # print statement is run using the f strings in which the variable names_tuple is passed to print the tuple

    names_sorted_as_list = sorted(names_tuple)
    # sorted tuple is assigned to a variable called names_sorted_as_list
    # Return a "new list" containing all items from the iterable in ascending order
    print(names_sorted_as_list)
    # printed the assigned to a variable called names_sorted_as_list

    names_sorted_as_list.append("Bungle")
    # append is the method which append object to the end of the list, hence "Bungle" is added at end of the list

    print("Added Bungle:", names_sorted_as_list)
    # printed the appended list with a string in front which describes that the "Bungle is appended at the end

    print("Attempt to manipulate the tuple...")
    # attempting to manipulate the tuple

    names_tuple[0] = 'Zippy'
    # attempted to add the object "Zippy" at the desirerd position of the collection
    # tuples are immutable hence the append won't go forward

    print("Is this code reached")
#     the print statement is not run as the code stops at the previous line as the tuple is immutable

# Exception handling: The except clause(s) specify one or more exception handlers
except FileNotFoundError as error:
    print("####### EXCEPT: TypeError #######")
    print("The EXCEPT / CATCH block only runs if this error happens")
    print(f"The following file cab bot be found: {error.filename}. Please try another file.")

# search inspects the except clauses in turn until one is found that matches the exception
except TypeError as error:
    print("###### EXCEPT: TypeError #########")
    print("Oh dear, that is not allowed on that type")
    print(error)

except Exception as error:
    print("######## EXCEPT: Exception ########")
    print("Generic catch-all except/catch block")
    print(error)

#     it specifies a ‘cleanup’ handler
# The try clause is executed, including any except and else clauses.
# If an exception occurs in any of the clauses and is not handled, the exception is temporarily saved.
# The finally clause is executed.
finally:
    # Always close file handle after use
    print("The FINALLY block ALWAYS runs")
    print("The finally block is used to tidy up")
    if names_tuple:
        names_tuple = None
# statement is printed as the conditional statement is met
print("After exception handling is finished..... the program can continue")