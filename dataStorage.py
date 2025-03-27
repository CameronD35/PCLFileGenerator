filePath = '/home/rsx25/Desktop/Data/test.pcd'

contentString = ''

# file = open(filePath, 'a')
# content = 'test stuff'
# file.write(content)
# file.close()

# width - width of geomrtry
# height - height of geometry
# resolution - distance between points
def generatePCDFlatGeometry(width, height, resolution):

    storageArray = []
    
    pointsPerRow = int(width / resolution)

    # The distance between each point in the row dimension (x-axis)
    rowRatio = width / pointsPerRow

    pointsPerColumn = int(height / resolution)

    # The distance between each point in the column dimension (z-axis)
    columnRatio = height / pointsPerColumn

    y = 5

    # Adding 1 to the loops since range does not include the upper bound
    for i in range (0, pointsPerRow + 1):

        xDistance = round((i * rowRatio), 5)

        for j in range (0, pointsPerColumn + 1):

            zDistance = round((j * columnRatio), 5)

            coordinateVector = (xDistance, 5, zDistance)
            
            storageArray.append(coordinateVector)

    return storageArray;

def setupPCDFile(filePath, geometryArray):
    arrLength = len(geometryArray)

    header = "# .PCD v.5 - Point Cloud Data file format"
    version = "VERSION .5"

    fieldFormat = {
        "x": [4, "F", 1],
        "y": [4, "F", 1],
        "z": [4, "F", 1]
    }

    fields = "x y z"
    size = "4 4 4"
    typ = "F F F" 
    count = "1 1 1"
    
    width = arrLength**0.5
    points = arrLength

    height = "1"

    data = "ascii"

    initialStr = f"{header}\n{version}\nFIELDS {fields}\nSIZE {size}\nTYPE {typ}\nCOUNT {count}\nWIDTH {width}\nHEIGHT {height}\nPOINTS {points}\nDATA {data}\n"

    file = open(filePath, 'w')
    file.write(initialStr)
    file.close()


def parseGeometryArray(geometryArray):

    file = open(filePath, 'a')


    for point in geometryArray:

        x = point[0]
        y = point[1]
        z = point[2]

        file.write(f"{x} {y} {z}\n")

    file.close()

test = generatePCDFlatGeometry(5, 5, 1)
setupPCDFile(filePath, test)
parseGeometryArray(test)


print(test)