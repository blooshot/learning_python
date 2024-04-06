import os
import shutil

cwd = "/home/k/Videos/Tutorials Hell/Code With Mosh - The Ultimate TypeScript Course"
cwd2 = "/home/k/Videos/Tutorials Hell/Code With Mosh - The Ultimate TypeScript Course/1 Welcome (2m)"
cwd3 = "/home/k/Videos/Tutorials Hell/Helloboy"
# typeScript = os.chdir(cwd)

def remove_second_last(array):
  if len(array) < 2:
    return array  # Handle cases with less than 2 elements

  return array[:len(array) - 2] + [array.pop()]

def changing_dir(filename,path):
    # print(path)
    srcPathArray = path
    # filename.endswith(".mp4")
    desPathArray = remove_second_last(path.split("/"))
    FinalDestination = "/".join(desPathArray)
    # print("SRC:"+srcPathArray)
    # print("DES:"+ds)
    try:
        # shutil.move(srcPathArray, FinalDestination)
        print("File moved successfully!: "+FinalDestination)
    except FileNotFoundError:
        print("Error: File not found at the source location.")
    except Exception as e:
        print(f"An error occurred during the move: {e}")

def recurxFolder (path):
    lsArray = os.listdir(path)
    i=0
    path = path + "/" +lsArray[i]
    # print(path)
    # print(newDir)
    if(os.path.isdir(path)):
        os.chdir(path)
        recurxFolder(path)
    else:
        filename = lsArray[0]
        changing_dir(filename,path)
        i = i + 1
       
def move_mp4s_to_parent(root_dir):

  for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        source = os.path.join(dirpath, filename)
        # destination = os.path.join(dirpath, os.path.dirname(filename))  # Parent folder
        newPathArray = remove_second_last(source.split("/"))
        destination = "/".join(newPathArray)

        try:
          shutil.move(source, destination)
          print(f"Moved '{filename}' from subfolder to parent: {destination}")
        except FileNotFoundError:
          print(f"Error: File '{filename}' not found at {source}")
        except Exception as e:
          print(f"An error occurred while moving '{filename}': {e}")

move_mp4s_to_parent(cwd)        
# startPointArray = os.listdir(cwd)
# for point1 in startPointArray:
#     print("fo:"+point1)

# recurxFolder(cwd)


# print(os.path.exists(cwd))
# # print(os.walk(cwd))
# for root, directories, files in os.walk(cwd):
#   print(f"Root directory: {root}")

#   # Print subdirectories
#   for directory in directories:
#     print(f"\tSubdirectory: {directory}")

#   # Print files (if any)
#   for filename in files:
#     print(f"\tFile: {filename}")
