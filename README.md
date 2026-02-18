# Algorithmic Trading Platform for Indian Stock Markets

A production-grade algorithmic trading platform supporting all stocks from BSE and NSE with a futuristic, professional interface. The platform follows a modular architecture with clear separation of concerns between market data, strategy engine, risk management, and execution layers.

## 🏗️ Architecture

The platform follows a decoupled service architecture:

```
Market Data Layer (BSE/NSE/TradingView APIs)
→ Strategy Engine (Modular, plug-and-play)
→ Risk Management Layer (Configurable via UI)
→ Execution Engine (Broker Integration)
→ Monitoring & Control System
```

## 🚀 Features

### Core Components
- **Market Data Layer**: Real-time streaming from BSE, NSE, and TradingView
- **Strategy Engine**: Plug-and-play strategies with backtesting support
- **Risk Management**: Comprehensive risk controls and kill switches
- **Execution Engine**: Order management and broker connectivity
- **Monitoring System**: Real-time dashboard with P&L tracking

### Technical Features
- **Backend**: Python (FastAPI) with asynchronous processing
- **Frontend**: React with TypeScript and Tailwind CSS
- **Database**: PostgreSQL for persistent data, Redis for caching
- **Containerization**: Docker and docker-compose for deployment
- **Real-time**: WebSocket connections for live data

## 📋 Prerequisites

- Python 3.11+
- Node.js 18+
- Docker and Docker Compose
- Access to Indian stock market data sources (BSE, NSE APIs)

## 🛠️ Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd algorithmic-trading-platform
```

2. Install backend dependencies:
```bash
cd backend
pip install -r requirements.txt
```

3. Install frontend dependencies:
```bash
cd ../frontend
npm install
```

4. Set up environment variables:
```bash
# Copy and edit environment files
cp .env.example .env
```

## 🚀 Running the Application

### Using Docker (Recommended)

```bash
# Build and start all services
docker-compose up --build

# Access the application:
# Backend API: http://localhost:8000
# Frontend UI: http://localhost:3000
```

### Running Manually

1. Start the backend:
```bash
cd backend
python main.py
```

2. Start the frontend:
```bash
cd frontend
npm run dev
```

## 📊 API Endpoints

### Market Data
- `GET /api/v1/stocks` - Get all available stocks
- `GET /api/v1/stocks/{symbol}` - Get current market data for a symbol
- `GET /api/v1/stocks/{symbol}/historical` - Get historical data
- `GET /api/v1/stocks/search` - Search for stocks

### Strategies
- `GET /api/v1/strategies` - Get all strategies
- `POST /api/v1/strategies` - Create a new strategy
- `POST /api/v1/strategies/{strategy_id}/activate` - Activate strategy
- `POST /api/v1/strategies/{strategy_id}/deactivate` - Deactivate strategy
- `POST /api/v1/strategies/{strategy_id}/backtest` - Run backtest

### Orders
- `POST /api/v1/orders` - Place a new order
- `GET /api/v1/orders` - Get active orders
- `GET /api/v1/orders/history` - Get order history
- `PUT /api/v1/orders/{order_id}/cancel` - Cancel an order

### Risk Management
- `GET /api/v1/risk/metrics` - Get current risk metrics
- `POST /api/v1/risk/kill-switch` - Apply kill switch to strategy
- `PUT /api/v1/risk/limits/update` - Update risk limits

## 🤖 Strategy Development

The platform supports modular strategy development:

1. Create a new strategy class extending `BaseStrategy`
2. Implement the `analyze()` method to generate signals
3. Register the strategy with the `@strategy_registry.register` decorator
4. Configure risk parameters via the API/UI

Example strategy:
```python
@strategy_registry.register
class MyStrategy(BaseStrategy):
    def get_required_data(self) -> List[str]:
        return ['price', 'volume']

    async def analyze(self, market_data: MarketData) -> Optional[StrategySignal]:
        # Your strategy logic here
        if condition:
            return StrategySignal(
                strategy_id=self.id,
                symbol=market_data.symbol,
                signal='BUY',
                confidence=0.8,
                strength=0.5,
                suggested_price=market_data.last_price,
                timestamp=market_data.timestamp
            )
        return None
```

## 🛡️ Risk Management

The platform implements comprehensive risk controls:

- Position sizing limits
- Daily loss limits
- Drawdown controls
- Correlation management
- Strategy-level kill switches
- Order-level risk validation

## 📈 Backtesting Framework

- Same code path for backtesting, paper trading, and live trading
- Accurate modeling of fees, slippage, and latency
- Performance metrics calculation
- Walk-forward testing support

## 🧪 Testing

Run backend tests:
```bash
cd backend
pytest
```

Run frontend tests:
```bash
cd frontend
npm test
```

## 🚢 Deployment

The platform is designed for containerized deployment:

1. Build Docker images:
```bash
docker-compose build
```

2. Deploy to production:
```bash
docker-compose -f docker-compose.prod.yml up -d
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new features
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🆘 Support

For support, please open an issue in the GitHub repository.