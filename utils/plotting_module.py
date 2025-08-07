import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import imageio
import os


def plotting_ozone(data_name, month_index, title, calendar_month, bar_min, bar_max, color, supplemental_info=False):
    """Function used when plotting monthly ozone easily
    
        Parameters
        ----------
        data_name : str
            Xarray DataArray you would like to plot, given it is multidimensional
        month_index : int
            Index for which you're plotting data_name
        title : str
            Title of the plot
        calendar_month : str
            Name of the month you're plotting for            
        bar_min : int
            Colorbar min value
        bar_max : int
            Colorbar max value
        color : str
            Matplotlib cmap color value
        supplemental_info : boolean, optional
            If the argument `supplemental_info` isn't passed in, no extra mean information will be added
            Default: no info added
        """
    plt.figure(figsize=(10, 6))
    ax = plt.axes(projection=ccrs.PlateCarree())
    data_name[month_index].plot(ax=ax,transform=ccrs.PlateCarree(central_longitude=0), vmin=bar_min, vmax=bar_max, extend='both', cmap=color)
    ax.add_feature(cfeature.COASTLINE, linestyle='--')
    ax.set_global()
    ax.set_facecolor('gray')

    # adding gridlines
    gl = ax.gridlines(draw_labels=True, color='black', alpha=0.5, linestyle='--')
    gl.right_labels = False

    # set title
    ax.set_title(f'{calendar_month[i]}', fontsize=18)
    plt.suptitle(title, 
                 fontsize=28, ha='right', x=0.2, fontweight='bold')

    if (supplemental_info==True):
        formatted_mean = f"{data_name[month_index].mean().data:.3f}"
        ax.text(0.10, -0.25, 'Mean: ' + str(formatted_mean) + ' DU', va='bottom', ha='center',
                rotation='horizontal', rotation_mode='anchor',
                transform=ax.transAxes, fontsize=12)

    plt.show()

def create_gif(image_folder, output_gif, duration, filename):
    """Function used when creating a gif of ozone maps
        Parameters
        ----------
        image_folder : str
            Path to where the PNGs you saved are
        output_gif : str
            Name of gif you would like to create
        duration : int
            How long every figure will be on the screen for, increments of 0.01 seconds
        filename : str
            What the PNGs you want to turn into a GIF start with
        """"
    filenames = sorted([f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))])
    images = []
    for filename in filenames:
        # include those files that start with certain characters (alternatively use .endswith(filename))
        if filename.startswith(filename):
            image_path = os.path.join(image_folder, filename)
            images.append(imageio.imread(image_path))
    imageio.mimsave(output_gif, images, duration=duration)