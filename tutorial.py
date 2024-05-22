import torch

from torchvision import datasets, transforms


def train(args, model, device, train_loader, optimizer, epoch):
    for _, _ in enumerate(train_loader):
        pass


print('Error')


class Config:

    def __init__(self) -> None:
        self.batch_size = 0
        self.test_batch_size = 0
        self.epochs = 0
        self.lr = 0.0
        self.momentum = 0.0
        self.no_cuda = False
        self.seed = 0
        self.log_interval = 0


config = Config()
config.batch_size = 16  # input batch size for training (default: 64)
config.test_batch_size = 10  # input batch size for testing (default: 1000)
config.epochs = 10  # number of epochs to train (default: 10)
config.lr = 0.1  # learning rate (default: 0.01)
config.momentum = 0.1  # SGD momentum (default: 0.5)
config.no_cuda = False  # disables CUDA training
config.seed = 42  # random seed (default: 42)
config.log_interval = 10  # how many batches to wait before logging training status


def main():
    use_cuda = not config.no_cuda and torch.cuda.is_available()

    kwargs = {'num_workers': 1, 'pin_memory': True} if use_cuda else {}

    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

    train_loader = torch.utils.data.DataLoader(datasets.CIFAR10(root='./data', train=True, download=True, transform=transform),
                                               batch_size=config.batch_size,
                                               shuffle=True,
                                               **kwargs)
    test_loader = torch.utils.data.DataLoader(datasets.CIFAR10(root='./data', train=False, download=True, transform=transform),
                                              batch_size=config.test_batch_size,
                                              shuffle=False,
                                              **kwargs)

    classes = ('plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

    model = None
    optimizer = None
    device = None
    for epoch in range(1, config.epochs + 1):
        train(config, model, device, train_loader, optimizer, epoch)


if __name__ == '__main__':
    main()
