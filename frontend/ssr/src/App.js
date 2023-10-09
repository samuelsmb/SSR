import logo from './logo.svg';
import './App.css';
import 'axios';
import axios from 'axios';


const ssr = axios.create({
  baseURL: `https://ssr.finanstilsynet.no/api/v2/instruments/`
})

ssr.get('/').then(( { data } ) => {
  var issuerName = data

  console.log(issuerName)
})



function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
