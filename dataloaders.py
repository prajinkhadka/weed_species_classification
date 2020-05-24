#For converting the dataset to torchvision dataset format
class DatasetLoader(Dataset):
    def __init__(self, file_path,label_path,train=True,transform=None):
        self.transform = transform
        self.file_path=file_path
        self.train=train
        self.label_path = label_path
        
        self.data_info = pd.read_csv(self.label_path)

        self.data_info = self.data_info.sort_values(by = ['Label'])
        self.data_info = self.data_info.reset_index()
        
        self.file_names = [file for _,_,files in os.walk(self.file_path) for file in files]
        self.file_names = sorted(self.file_names)
        self.file_names = np.array(self.file_names)
        self.file_names = self.file_names[:17508]
        

        
        self.len = len(self.file_names)
        
        
    def __len__(self):
        return len(self.file_names)
    
    def __getitem__(self,  index):
        file_name = self.file_names[index]
        image_data = self.pil_loader(self.file_path +"/" + file_name)
        if self.transform:
            image_data = self.transform(image_data)
        if self.train:
            Y1 = self.get_classes(index)
            label = Y1
            return image_data, label
            
            

    
    
    def pil_loader(self, path):
        with open(path, 'rb') as f:
            img = Image.open(f)
            image_data = img.convert('RGB')
            return image_data
    
    def get_classes(self, index):
        classs = self.data_info['Species'][index]
        
        return classs
    