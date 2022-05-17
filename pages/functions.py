#Define Plotting function

def add_metricBar(value = 0, title = "Title", value_prev = 0, min_val = 0, max_val = 0, buy_bnd = 0, mid_bnd = 0, sell_bnd = 0, x = [0,0], y = [0,0]):
    import plotly.graph_objects as go

    if value < buy_bnd:
        scenario = "Bottom"
        bar_color = "green"
    elif value < mid_bnd:
        scenario = "Mid Low"
        bar_color = "gold"
    elif value < sell_bnd:
        scenario = "Mid High"
        bar_color = "orange"
    else:
        scenario = "Peak"
        bar_color = "red"
    
    fig.add_trace(go.Indicator(
    mode = "number+gauge+delta", value = value,
    
    number = {"suffix":" "+scenario,
             "font":{"color":bar_color}},
    
    delta = {'reference': value_prev, "relative":True},
    
    domain = {'x': x, 'y': y},
    
    title = {'text': title},
    
    gauge = {
        'shape': "bullet",
        
        'axis': {'range': [min_val, max_val]},
        
        'threshold': {
            'line': {'color': "black", 'width': 2},
            'thickness': 0.75,
            'value': value_prev},
        
        'steps': [
            {'range': [min_val, buy_bnd], 'color': "yellowGreen"},
            {'range': [buy_bnd, mid_bnd], 'color': "lightGoldenRodYellow"},
            {'range': [mid_bnd, sell_bnd], 'color': "moccasin"},
            {'range': [sell_bnd, max_val], 'color': "tomato"}],
        
        'bar': {'color': bar_color}}))