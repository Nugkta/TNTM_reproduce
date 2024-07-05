import octis 
from stream.data_utils.dataset import dataset

class OctisDataset2StreamDataset(dataset):
    """
    A class that takes an octis dataset and turns it into a stream dataset
    """

    def __init__(
            self,
            octis_dataset,
    ):
        """
        Args:
            octis_dataset: an octis dataset
        """
        super().__init__()
        
        # make all the attributes of the octis dataset available

        for key, value in octis_dataset.__dict__.items():
            setattr(self, key, value)

