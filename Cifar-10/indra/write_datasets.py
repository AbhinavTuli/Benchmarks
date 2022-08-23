import hub

if __name__ == "__main__":
    hub.deepcopy("hub://activeloop/cifar10-train", "/tmp/cifar10_train_hub")
    hub.deepcopy("hub://activeloop/cifar10-test", "/tmp/cifar10_test_hub")