Dataset = {
  "listA": [{
    "name": "John",
    "age": 20,
    "dateJoined": "2020-01-01",
  }, {
    "name": "John",
    "age": 25,
    "dateJoined": "2020-01-01",
  }, {
    "name": "John",
    "age": 30,
    "dateJoined": "2020-01-01",
  }, {
    "name": "Alice",
    "age": 35,
    "dateJoined": "2020-01-01",
  }, {
    "name": "Joe",
    "age": 40,
    "dateJoined": "2020-09-25",
  }],
  "listB": [{
    "name": "Kate",
    "age": 20,
    "dateJoined": "2020-01-01",
  }, {
    "name": "Lisa",
    "age": 21,
    "dateJoined": "2019-12-23",
  }, {
    "name": "mike",
    "age": 30,
    "dateJoined": "2020-04-26",
  }, {
    "name": "nancy",
    "age": 35,
    "dateJoined": "2020-08-20",
  }, {
    "name": "peter",
    "age": 40,
    "dateJoined": "2020-03-25",
  }
]
}

# test User data, used to test the sorting algorithm

def quickSort(arr, left, right, parameter):
  # implementation of the quick sort algorithm based on the parameter 
    def partition(arr, left, right, pivot):
        while left <= right:
            while arr[left][parameter] < pivot[parameter]:
                left +=1
            while arr[right][parameter] > pivot[parameter]:
                right -=1
            if left <= right:
                # swap the values on the right and left of the pivot point
                temp = arr[left]
                arr[left] = arr[right]
                arr[right] = temp
                # go into the list from both ends after swapping
                left += 1
                right -=1
        return left
    if left >= right:
        return 
    # pivot point is always selected from the midpoint
    pivot = arr[int((left + right)/2)]
    index = partition(arr, left, right, pivot)
  
    quickSort(arr, left, index - 1, parameter)
    quickSort(arr, index, right, parameter)





def mergeSort(listA, listB):
    # perform a quick sort on the merged list
    mergedList = listA + listB
    quickSort(arr=mergedList, left=0, right=len(mergedList) - 1, parameter="dateJoined")
    dates = []

    for i in mergedList:
        # store all the dateJoined values of all users in the data array
        print(i)
        dates.append(i["dateJoined"])


    def getRepeatedValues(list):
      # this function checks for repeated value
        repeated_values = {}
        count = 1
        for i in range(len(list)):
            if i < count:
              # skip indexes if they are the same
                continue
            index_dates= [i]
            index_names = [mergedList[i]["name"]]
            for j in range(i+1, len(list)):
                if list[i] == list[j]:
                  # compare the first element in the list to the next element 
                  # if equal increase count
                    count +=1
                    index_dates.append(j)
                    index_names.append(mergedList[j]["name"])
                    repeated_values.update({list[i]: (index_dates, index_names)})
                    if j >= len(list) - 1:
                      # end function of j is at the end of the loop
                      return repeated_values
                else:
                    # break if next element is not equal
                    break

        print(repeated_values)
        return repeated_values
    
    # get all indexes of users with the same dateJoined
    repeated_dates = getRepeatedValues(dates).items()
    for key , value in repeated_dates:
      # sort the list based on names using the quick sort if dates are repeated
      quickSort(mergedList, value[0][0], value[0][len(value[0])-1], "name")
      names = [i for i in value[1]]
    # get all the names of users with the same dateJoined
      repeated_names = getRepeatedValues(names).items()
      for key2, value2 in repeated_names:
        # sort the list based on ages using the quick sort if names are repeated
        quickSort(mergedList, value2[0][0], value2[0][len(value2[0])-1], "age")


    print("\n\n")
    for i in mergedList:
        print(i)

mergeSort(Dataset["listA"], Dataset["listB"])
