import numpy as np

def apply_default_matplotlib_styling(fig, axs, title, 
                xaxis_title=None, yaxis_title=None):
    # Set the figure title
    fig.suptitle(title, fontsize=24, fontname="Arial", color="black", 
                 y=0.95, x=0.5, ha='center', va='top')
    
    # Check if axs is a single Axes object or an array of Axes
    if not isinstance(axs, np.ndarray):
        axs = [axs]

    # Flatten the array if it is multi-dimensional
    axs = np.ravel(axs)

    # Set axis labels and customize tick labels for each subplot
    for ax in axs:
        if xaxis_title:
            ax.set_xlabel(xaxis_title, fontsize=14, 
                          fontname="Arial", color="black")
        if yaxis_title:
            ax.set_ylabel(yaxis_title, fontsize=14, 
                          fontname="Arial", color="black")
        
        for label in (ax.get_xticklabels() + ax.get_yticklabels()):
            label.set_fontname("Arial")
            label.set_fontsize(14)
            label.set_color("black")
    
    return fig, axs


def apply_default_plotly_styling(fig, title, xaxis_title=None, 
                          yaxis_title=None, legend_title=None):
    """ Function to update layout with consistent styling and flexible parameters

    Args:
        fig (plotly.graph_objects.Figure): Figure for formatting
        title (str): Main title for graph
        xaxis_title (str): Title for x-axis of graph
        yaxis_title (str): Title for y-axis of graph

    Returns:
        plotly.graph_objects.Figure: Plotly figure with updated formatting
    """    
    # Update layout for title and fonts
    fig.update_layout(
        title={
            'text': title,
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        font=dict(
            family="Arial, sans-serif",
            size=14,
            color="black"
        ),
        title_font=dict(size=24)
    )

    if xaxis_title is not None:
        fig.update_layout( xaxis_title=xaxis_title)

    if yaxis_title is not None:
        fig.update_layout(yaxis_title=yaxis_title)

    if legend_title is not None:
        fig.update_layout(legend_title_text=legend_title)
    
    return fig


def add_bar_totals(fig, df, col, y_offset=1000):
    """Adds sum of stacked bar graph to each column

    Args:
        fig (plotly.graph_objects.Figure): Figure to update
        df (pd.DataFrame): DF with totals to add
        col (str): Column name from df with relevant totals
        y_offset (int, optional): How far to move title vertically. Defaults to 1000.

    Returns:
        plotly.graph_objects.Figure: Plotly stacked bar graph with totals annotated
    """    
    total_counts = df[col].to_list()
    for i, total in enumerate(total_counts):
        fig.add_annotation(
            x=i,
            y=total + y_offset,
            yanchor='top',
            text=str(total),
            showarrow=False,
            font=dict(
                family="Arial, sans-serif",
                size=14,
                color="black"
            ),
        )
    return fig