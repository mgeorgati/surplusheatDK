import matplotlib.colors as colors
from matplotlib.colors import ListedColormap
import contextily as cx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def plot_map(df, column_to_map, namefile,  year):
    bin_edges = [0, 2.5, 5, 10, 25, 100]  # Define bin edges as per your requirement

    bins = 5
    colors_palette = ["#eaac8b", "#e56b6f", "#b56576","#6d597a", "#355070"]

    cmap = ListedColormap(colors_palette)
    norm = colors.BoundaryNorm(bin_edges, bins)  

    # Add a legend for labels
    legend_labels = { colors_palette[0]: "{0}-{1}".format(bin_edges[0], bin_edges[1]), colors_palette[1]: "{0}-{1}".format(bin_edges[1], bin_edges[2]), 
    colors_palette[2]: "{0}-{1}".format(bin_edges[2],bin_edges[3]), colors_palette[3]: "{0}-{1}".format(bin_edges[3],bin_edges[4]),
    colors_palette[4]: ">{0}".format(bin_edges[4],bin_edges[5])}

    #df['cut_Number of new DH Plants'] = pd.cut(df["Number of new DH Plants"], bins=bin_edges, labels=bin_labels, include_lowest=True)
    fig, ax = plt.subplots(figsize=(8, 10))
    df.plot(ax=ax, column=column_to_map, cmap=cmap , norm=norm, alpha=0.85, ) #alpha=0.55,

    df.plot(ax=ax, facecolor='none', edgecolor='#858585', linewidth=0.1,  zorder=17  ) #alpha=0.8,
    df['coords']= df['geometry'].apply(lambda x: x.representative_point().coords[:])
    df['coords'] = [coords[0] for coords in df['coords']]
    for idx, row in df.iterrows():
        plt.annotate(text = row['municipality_name_shorted'], xy=row['coords'], horizontalalignment= 'center', fontsize=6, font='Calibri' ,zorder=20) 

    # Set the bounding box (xmin, xmax, ymin, ymax)
    xmin = 870770
    xmax = 1435400
    ymin= 7262120 
    ymax = 7930000 
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax) 

    ax.set_axis_off()
    cx.add_basemap(ax, source=cx.providers.CartoDB.Positron,attribution="")

    patches = [mpatches.Patch(color=color, label=label)
                for color, label in legend_labels.items()]
    ax.legend(handles=patches, loc='upper right', facecolor="white", fontsize=7, 
              title = "SH contribution to\ntotal DH production (%)", title_fontsize=8)
    if year >0:
        plt.title(f"{year}", fontsize=7 )
    plt.savefig(f'../img/{namefile}_{year}.png', dpi=300, bbox_inches='tight', 
                facecolor=fig.get_facecolor(),transparent=True) 

    plt.cla()
    plt.close()
