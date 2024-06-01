function train(model, train_data, epochs, mini_batch_size, loss_function, optimizer):
    # Initialize dataloaders for mini-batch and full-batch
    mini_batch_loader = DataLoader(train_data, batch_size=mini_batch_size, shuffle=True)
    full_batch_loader = DataLoader(train_data, batch_size=len(train_data), shuffle=True)

    for epoch in range(epochs):
        model.train()
        total_loss = 0
        
        if epoch % 2 == 0:
            print("Epoch {}/{} - Full Batch Training".format(epoch + 1, epochs))
            for batch in full_batch_loader:
                inputs, targets = batch
                # Forward pass
                predictions = model.forward(inputs)
                loss = loss_function(predictions, targets)
                
                # Backward pass and optimization
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()
                
                total_loss += loss.item()
        else:
            print("Epoch {}/{} - Mini Batch Training".format(epoch + 1, epochs))
            for batch in mini_batch_loader:
                inputs, targets = batch
                # Forward pass
                predictions = model.forward(inputs)
                loss = loss_function(predictions, targets)
                
                # Backward pass and optimization
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()
                
                total_loss += loss.item()
        
        # Calculate average loss for the epoch
        avg_loss = total_loss / (len(full_batch_loader) if epoch % 2 == 0 else len(mini_batch_loader))
        print("Epoch {}/{} - Loss: {:.4f}".format(epoch + 1, epochs, avg_loss))

# Helper functions
function DataLoader(dataset, batch_size, shuffle):
    if shuffle:
        dataset = shuffle_dataset(dataset)
    return split_into_batches(dataset, batch_size)

function shuffle_dataset(dataset):
    # Implement dataset shuffling logic
    shuffled_dataset = random.shuffle(dataset)
    return shuffled_dataset

function split_into_batches(dataset, batch_size):
    # Split dataset into batches of size batch_size
    batches = []
    for i in range(0, len(dataset), batch_size):
        batch = dataset[i:i + batch_size]
        batches.append(batch)
    return batches
