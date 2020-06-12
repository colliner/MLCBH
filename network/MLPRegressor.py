from sklearn.neural_network import MLPRegressor

model = MLPRegressor(
      activation='relu',
      alpha='0.5', 
      learning_rate_init='0.0001', 
      max_iter=50000, 
      early_stopping=False,
      hidden_layer_sizes=(51,), 
      n_iter_no_change=25, 
      tol=0.0001,
      batch_size=200,   # or min(200,n_samples)
      shuffle=True,
      solver='adam', 
      beta_1=0.9, beta_2=0.999, epsilon=1e-08,     # ADAM defaults
      verbose=False)
