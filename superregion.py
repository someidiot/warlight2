class SuperRegion(object):
    '''
    Super Region class
    '''
    def __init__(self, super_region_id, worth):
        '''
        Initializes with an id, the super region's worth and an empty lists for 
        regions located inside this super region
        '''
        self.id = super_region_id
        self.worth = worth
        self.regions = []
