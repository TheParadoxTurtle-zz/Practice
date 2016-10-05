import fractions

def answer(vertices):
    x_l = 1000000001
    y_l = 1000000001
    x_h = -1000000001
    y_h = -1000000001
    borderCount = [0]*3
    for i in range(0, 3):
        v = vertices[i]
        if x_l > v[0]:
            x_l = v[0]
        if x_h < v[0]:
            x_h = v[0]
        if y_l > v[1]:
            y_l = v[1]
        if y_h < v[1]:
            y_h = v[1]
    for i in range(0, 3):
        v = vertices[i]
        if x_l == v[0] or x_h == v[0]:
            borderCount[i] += 1
        if y_l == v[1] or y_h == v[1]:
            borderCount[i] += 1
    
    bound = (x_h - x_l + 1)*(y_h - y_l + 1)
    A = vertices[0]
    B = vertices[1]
    C = vertices[2]
    bound -= rightTriangleWithBorder(A, B)
    bound -= rightTriangleWithBorder(B, C)
    bound -= rightTriangleWithBorder(C, A)
    bound += 3
    
    print borderCount
 
    if borderCount[0] == 0:
        bound -= missingSquare(A, [B[0], C[1]], [B[1], C[0]]) 
    elif borderCount[1] == 0:
        bound -= missingSquare(B, [A[0], C[1]], [A[1], C[0]]) 
    elif borderCount[2] == 0:
        bound -= missingSquare(C, [B[0], A[1]], [B[1], A[0]]) 
    
    return bound
    
def rightTriangleWithBorder(A, B):
    length = abs(A[0] - B[0])
    height = abs(A[1] - B[1])
    #in triangle + border = (total - diag)/2 + diag
    
    if length == 0 or height == 0:
        return length + height + 1
        
    diag = fractions.gcd(length, height) + 1
    
    total = (length+1)*(height+1)
    
    return (total - diag)/2 + diag
    
#Square of lattice points missed if point X
#is not on the border of the bounding box
#D and E are the other corner points
#note that two sides must be excluded from this calculation
def missingSquare(X, D, E):
    dist_D = (X[0] - D[0])**2 + (X[1] - D[1])**2
    dist_E = (X[0] - E[0])**2 + (X[1] - E[1])**2
    
    length = 0
    height = 0
    if dist_D < dist_E:
        length = abs(X[0] - E[0])
        height = abs(X[1] - E[1])
    else:
        length = abs(X[0] - E[0])
        height = abs(X[1] - E[1])
	
    print length        
    print height        
    print D        
    print E        
    return (length + 1)*(height+1) - length - height - 1
    
    
    

print answer([[2, 3], [6, 9], [10, 160]])
#print answer([[91207, 89566], [-88690, -83026], [67100, 47194]])
