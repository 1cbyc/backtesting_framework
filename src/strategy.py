class ICTStrategy:
    def enter_trade(self, market_data):
        """
        my plan here is to determine the entry signal
        say, i do:
        Args:
            market_data (DataFrame): Historical price data.
        Returns:
            dict: Signal with details (e.g., entry price, trade type).
        :param market_data:
        :return:
        """
        raise NotImplementedError("Subclasses should implement this method.")

    def exit_trade(self, market_data):
        """
        my plan here is to determine the entry signal
        say, i do:
        Args:
            market_data (DataFrame): Historical price data.
        Returns:
            dict: Signal with details (e.g., exit price, trade type).
        :param market_data:
        :return:
        """
        raise NotImplementedError("Subclasses should implement this method.")