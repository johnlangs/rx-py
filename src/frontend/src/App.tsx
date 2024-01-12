import { useCallback, useEffect, useState } from 'react'
import './App.css'

type med = {
  'name': string,
  'Therapeutic area': string,
  'Condition / indication': string,
  'URL': string
}

function App() {
  const [query, setQuery] = useState('relapsing remitting multiple sclerosis');

  const [meds, setMeds] = useState<med[]>(new Array<med>(5).fill({
    'name': '',
    'Therapeutic area': '',
    'Condition / indication': '',
    'URL': ''
  }));

  const search = async () => {
    const requestBody = {
      query: query
    }

    const response = await fetch('http://127.0.0.1:5000/search', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(requestBody),
    });

    const data: med[] = await response.json();

    setMeds(data);
  }

  useEffect(() =>{
    search();
  }, [query]);

  return (
    <div className="flex items-center justify-center h-screen">
      <div className="max-w-lg">
        <h1 className='font-bold text-4xl text-center mb-10'>Rx.py</h1>
    
        <input type="text" onChange={e => setQuery(e.target.value)} value={query} className="input input-bordered input-secondary w-full max-w-lg mb-10" />

        <div className="join join-vertical w-full max-w-lg">
          {
            meds.map((value, index) => (
              <div key={index} className="collapse collapse-arrow join-item border border-base-300">
              <input type="radio" name="my-accordion-4" /> 
              <div className="collapse-title text-xl font-medium">
                {value.name}
              </div>
              <div className="collapse-content"> 
                <p>Therapeutic area: {value['Therapeutic area']}</p>
                <br/>
                <p>Condition / indication: {value['Condition / indication']}</p>
                <br/>
                <p><a href={value['URL']} className="link link-secondary">More Info</a></p>
              </div>
            </div>
            ))
          }
        </div>
      </div>
    </div>
  )
}

export default App
