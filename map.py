class Map(object):
    '''
    Map class
    '''
    def __init__(self):
        '''
        Initializes empty lists for regions and super regions.
        '''
        self.regions = []
        self.super_regions = []

    def get_region_by_id(self, region_id):
        '''
        Returns a region instance by id.
        '''
        return [region for region in self.regions if region.id == region_id][0]
    
    def get_super_region_by_id(self, super_region_id):
        '''
        Returns a super region instance by id.
        '''
        return [super_region for super_region in self.super_regions if super_region.id == super_region_id][0]

    def get_owned_regions(self, owner):
        '''
        Returns a list of region instances owned by `owner`.
        '''
        return [region for region in self.regions if region.owner == owner]