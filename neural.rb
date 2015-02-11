require 'ai4r'
require 'RMagick'

module Sr
  class Brain
    GRID_SIZE=13
	GRID_SIZE2=22
	def black?(p)
       return p.intensity == 0 || (Magick::QuantumRange.to_f / p.intensity) < 0.5
    end
    def initialize
	  
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
  end
  
 foo = Brain.new 
 @arr=('a'..'z').to_a + ('0'..'9').to_a
 #for i in @arr
 i='5'
 path = "C:/Users/Prasanth/Desktop/"+i+".gif"
  x=Magick::Image.read(path)[0]
 
	foo.train(i,x)


#end
 print foo.classify_all(x)
  
end


