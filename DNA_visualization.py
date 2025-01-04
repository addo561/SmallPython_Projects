import random, sys, time

class DNA:
    def __init__(self, pause, ROWS):
        self.pause = pause
        self.ROWS = ROWS
        self.rightnucleotide = ' '
        self.leftnucleotide = ' '
        self.rowIndex = 0

    def draw(self):
        try:
            print('DNA Animation')
            print('Press Ctrl-C to quit...')
            time.sleep(2)

            while True:
                self.rowIndex += 1  # Increment rowIndex to draw next row
                if self.rowIndex == len(self.ROWS):
                    self.rowIndex = 0  # Reset to the first row after the last.

                # Row indexes 0 and 9 don't have nucleotides:
                if self.rowIndex == 0 or self.rowIndex == 9:
                    print(self.ROWS[self.rowIndex])
                    continue

                # Select random nucleotide pairs: A-T or G-C
                randomSelection = random.choice('ATGC')  
                if randomSelection == 'A':
                    self.leftnucleotide, self.rightnucleotide = 'A', 'T'
                elif randomSelection == 'T':
                    self.leftnucleotide, self.rightnucleotide = 'T', 'A'
                elif randomSelection == 'G':
                    self.leftnucleotide, self.rightnucleotide = 'G', 'C'
                elif randomSelection == 'C':
                    self.leftnucleotide, self.rightnucleotide = 'C', 'G'  
                # Print the row with the nucleotide pair.
                self.printRow()

                # Pause before the next row.
                time.sleep(self.pause)

        except KeyboardInterrupt:
            sys.exit()  # Exit when Ctrl-C is pressed.

    def printRow(self):
        # Use the format method to insert the nucleotides into the row.
        print(self.ROWS[self.rowIndex].format(self.leftnucleotide, self.rightnucleotide))


# These are the individual rows of the DNA animation:
ROWS = [
    '          ##',  # Index 0 has no {}.
    '         #{}-{}#',
    '        #{}---{}#',
    '       #{}-----{}#',
    '      #{}------{}#',
    '     #{}------{}#',
    '     #{}-----{}#',
    '      #{}---{}#',
    '      #{}-{}#',
    '        ##',  # Index 9 has no {}.
    '       #{}-{}#',
    '       #{}---{}#',
    '      #{}-----{}#',
    '      #{}------{}#',
    '       #{}------{}#',
    '         #{}-----{}#',
    '           #{}---{}#',
    '            #{}-{}#'
]

# Create the DNA object and run the animation.
DNA_animation = DNA(0.15, ROWS)
DNA_animation.draw()
