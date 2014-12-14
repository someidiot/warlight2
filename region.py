class Region(object):
    '''
    Region class
    '''
    def __init__(self, region_id, super_region):
        '''
        '''
        self.id = region_id
        self.owner = 'neutral'
        self.neighbours = []
        self.troop_count = 2
        self.is_wasteland = False       # if true, the troop_count will be more than 2. is it always 10?
        self.super_region = super_region
        self.is_on_super_region_border = False