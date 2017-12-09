import math

# get prime number = p

def fft(a):

	# does fast fourier transform
    if len(a) == 1:
        return a
    else:
        # Split the sequence into even and odd
        a_even = [a[i] for i in range(len(a)) if i % 2 == 0]
        a_odd = [a[i] for i in range(len(a)) if i % 2 == 1]
    
        # perform Fast Fourier T.
        a_even = fft(a_even)
        a_odd = fft(a_odd)

        r = [0] * len(a)
        n_max = len(a) // 2
        
	# principle root of unity (w^1)
	# e^(2(pi)/2)
        e_exponent = (2 * math.pi) / len(a)
        w = complex(math.cos(e_exponent), math.sin(e_exponent))
        
	# [0, n_max - 1] = [0, (len(a) // 2) - 1]
        for i in range(n_max):
	    #print(w ** i)
	    #print(i)
            r[i]         = (a_even[i] + (w ** i) * a_odd[i])
            #r[i] = complex(r[i].real % p, r[i].imag)

            #r[i].real 	 = r[i].real % p
            r[i + n_max] = (a_even[i] - (w ** i) * a_odd[i])

            #r[i + n_max] = complex(r[i + n_max].real % p, r[i + n_max].imag)
        #print(r)
        #print()
        return r

def fftInverse(a):
    #print("a", a)
    a = fft(a)
    #print("fft(a)", a)
    length_a = len(a)
    # [len(a) - 1, 1]
    inverted = [a[0]] + [a[i] for i in range(len(a) - 1, 0, -1)]
    return [complex(element.real / length_a, element.imag / length_a) for element in inverted]

def pad(a):
    power_of_2 = 1
    length_a = len(a)
    while length_a > power_of_2:
        power_of_2  = power_of_2 * 2
    # add 0's to a so len(a) is a power of 2
    a = a + [0 for i in range(power_of_2 - length_a)]
    # have to double the size with 0's after the padding has been added
#    print(a)
    a = a + [0 for i in range(len(a))]
#    print(a)
    
    return (a)


def multFFT(a, b, p):
        # takes in
    a = pad(a)
    b = pad(b)
    a = fft(a)
    b = fft(b)
    #print("fft(a)", a)
    #print("fft(b)", b)
    #c = []
    #for i in range(len(a)):
    #	next_item = a[i] * b[i]
    	#next_item = complex(next_item.real % p, next_item.imag)
    #	c.append(next_item)
    c = [a[i] * b[i] for i in range(len(a))]
    #print("c", c)
    #d = cooefficients(a, b)
    #print("d", d)
    c = fftInverse(c)
    answer = [round(a.real) % p for a in c]
    #print(answer)
    for i in range(len(answer) - 1, -1, -1):
        if answer[i] == 0:
            del answer[i]
        else:
            break
    return answer

print(multFFT([1, 1, 1], [-1, 2, 0, 1], 7))
print("next problem")
print(multFFT([1, 0, 2, 5], [2, 0, 0, 3], 7))

