  mkdir -p ~/.streamlit/
		
  echo "\
  [global]
  dataFrameSerialization='legacy'
  [theme]\n\
  primaryColor='#2186E1'\n\
  backgroundColor='#FFFFFF'\n\
  secondaryBackgroundColor='#f0f2f6'\n\
  textColor='#262730'\n\
  font='sans serif'\n\
  [server]\n\
  maxUploadSize = 500\n\
  headless = true\n\
  port = $PORT\n\
  enableCORS=false\n\
  " > ~/.streamlit/config.toml
