"""You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.

Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a walk, that's standing still!)."""

def is_valid_walk(walk):

    def walk_north(co_ordinates):
        co_ordinates[1] += 1
        return co_ordinates

    def walk_south(co_ordinates):
        co_ordinates[1] -= 1
        return co_ordinates

    def walk_east(co_ordinates):
        co_ordinates[0] += 1
        return co_ordinates

    def walk_west(co_ordinates):
        co_ordinates[0] -= 1
        return co_ordinates
    
    def walking(direction, co_ordinates):
        if direction == "n":
            walk_north(co_ordinates)
        elif direction == "s":
            walk_south(co_ordinates)
        elif direction == "e":
            walk_east(co_ordinates)
        elif direction == "w":
            walk_west(co_ordinates)
        return co_ordinates

    def walk_is_long_enough(walk):
        return len(walk) == 10
    
    if not walk_is_long_enough(walk):
        return False
    
    co_ordinates = [0, 0]
    
    for instruction in walk:
        co_ordinates = walking(instruction, co_ordinates)
    
    return co_ordinates == [0, 0]
    
    
        