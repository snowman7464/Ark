import React from 'react'
import ReactDOM from 'react-dom/client'

const App = () => (
  <div style={{ textAlign: 'center', padding: '2em', fontFamily: 'sans-serif' }}>
    <h1>🦖 BreedTree ベータ版へようこそ！</h1>
    <p>この画面が見えていれば、Vercelデプロイ成功です！</p>
  </div>
)

ReactDOM.createRoot(document.getElementById('root')).render(<App />)
