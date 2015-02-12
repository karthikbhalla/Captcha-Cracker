require 'rubygems'
require 'ai4r'
require 'RMagick'

module Sr
 
  class Brain
    GRID_SIZE=15
	GRID_SIZE2=25
	
	def black?(p)
       return p.intensity == 0 || (Magick::QuantumRange.to_f / p.intensity) < 0.5
    end
    def initialize
	  @xdatas=Hash.new
      @keys  = *(('a'..'z').to_a + ('0'..'9').to_a)
      @ai = Ai4r::NeuralNetwork::Backpropagation.new([GRID_SIZE * GRID_SIZE2,
                                                      @keys.size])
	  
    end

    # Returns a flat array of 0 or 1 from the image data, suitable for
    # feeding into the neural network
    def to_data(image)
      # New image of our actual grid size, then paste it over
      padded = Magick::Image.new(GRID_SIZE, GRID_SIZE2)
      padded = padded.composite(image,
                                Magick::NorthWestGravity,
                                Magick::MultiplyCompositeOp)

      padded.get_pixels(0, 0, padded.columns, padded.rows).map do |p|
        black?(p) ? 1 : 0
      end
    end

    # Feed this a positive example, e.g., train('a', image)
    def train(char, image)
      outputs = [0] * @keys.length
      outputs[ @keys.index(char) ] = 1.0
      @ai.train(to_data(image), outputs)
    end
	def trainch(char)
      outputs = [0] * @keys.length
      outputs[ @keys.index(char) ] = 1.0
      @ai.train(@xdatas[char], outputs)
    end

    # Return all guesses, e.g., {'a' => 0.01, 'b' => '0.2', ...}
    def classify_all(image)
      results = @ai.eval(to_data(image))
      r = {}
      @keys.each.with_index do |v, i|
        r[v] = results[i]
      end
      r
    end

    # Returns best guess
    def classify(image)
      res = @ai.eval(to_data(image))
      @keys[res.index(res.max)]
    end
	def classifyfast(i)
      res = @ai.eval(@xdatas[i])
      @keys[res.index(res.max)]
    end
	
	def puttoxdata(image,i)
	@xdatas[i]=to_data(image)
	end
  end

 foo = Brain.new 
 @arr=('a'..'z').to_a + ('0'..'9').to_a
 x=Hash.new

  for i in @arr
  path = "E:/New folder/"+i+".gif"
  x[i]=Magick::Image.read(path)[0]
  foo.puttoxdata(x[i],i)
  end
  
   loop do
  print "Enter the number of iterations:"
  num_itr=gets.to_i
 for j in 0..num_itr
 for i in @arr

	#print "training " + i +":"+path
	
	foo.trainch(i)
	

end
if(j%10==0)
correct=0
for k in @arr

 if k===foo.classifyfast(k)
	correct=correct+1
 else

end
end
print "no of correct after #{j} iteration :#{correct} \n"
end
end
# path = "C:/Users/Prasanth/Desktop/y.gif"
# x=Magick::Image.read(path)[0]
 # print foo.classify(x)
# path = "C:/Users/Prasanth/Desktop/e.gif"
# x=Magick::Image.read(path)[0]
 # print foo.classify(x)
 # path = "C:/Users/Prasanth/Desktop/d.gif"
# x=Magick::Image.read(path)[0]
 # print foo.classify(x)
 # path = "C:/Users/Prasanth/Desktop/u.gif"
# x=Magick::Image.read(path)[0]
 # print foo.classify(x)
 print "cannot recognize:"
for k in @arr

 if k===foo.classifyfast(k)
	
 else
	print "#{k}	"
end
end
 print "\nEnter the filename to recognize:"
 n=gets[0]
 path = "E:/New folder/#{n}.gif"
 x=Magick::Image.read(path)[0]
 print foo.classify(x)
 print "\nContinue?:"
 val=gets[0]
 if val=='n' 
	break
	end
end
end



