from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook
from qtile_extras import widget as extrawidgets
import subprocess
import os

# MASTER KEY DEFINITION : 

mod = "mod4"
terminal = guess_terminal()




#AUTOSTART:

@hook.subscribe.startup
def autostart():
     home = os.path.expanduser('~/.config/qtile/autostart.sh')
     subprocess.Popen([home])




# KEYBOARD SHORTCUTS :

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "LEFT", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "RIGHT", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "DOWN", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "UP", lazy.layout.up(), desc="Move focus up"),

    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.


    # Moving out of range in Columns layout will create new column.

    Key([mod, "shift"], "LEFT", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "RIGHT", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "DOWN", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "UP", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction

    # will be to screen edge - window would shrink.

    Key([mod, "control"], "LEFT", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "RIGHT", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "DOWN", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "UP", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    Key([mod, "mod1"], "LEFT", lazy.layout.swap_column_left(),desc="Move column to the left"),
    Key([mod, "mod1"], "RIGHT", lazy.layout.swap_column_right(),desc="Move column to the right"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes

    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    #Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # Custom key

    Key([mod], "r", lazy.spawn("rofi -show drun"), desc="Rofi"),
    Key([mod], "XF86AudioLowerVolume", lazy.spawn("ddcutil --bus=8 setvcp 10 - 10")),
    Key([mod], "XF86AudioRaiseVolume", lazy.spawn("ddcutil --bus=8 setvcp 10 + 10")),

]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)

for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


groups = [Group(i) for i in "123"]

for i in groups:
    keys.extend(
        [
            # mod1 + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )
  

# LAYOUT, CUTTING BEHAVIOR :


layouts = [
    layout.Columns(border_focus=["#8A2BE2", "000000", "#8A2BE2", "000000"], border_width=6, num_columns=3, margin=10),
    layout.Max(),
    ]


# DEFAULT WIDGET VISUAL CONFIG :


widget_defaults = dict(
    font="sans bold",
    fontsize=16,
    padding=3,
)

extension_defaults = widget_defaults.copy()



# SCREEN AND TOP BAR : 

screens = [
    Screen(
        top=bar.Bar(
            [
                #widget.CurrentLayout(),
                widget.Spacer(
                    length = 45,
                    align="left",
                    ),
                widget.GroupBox(
                    fontsize=16, 
                    border_color="#06038D", 
                    active="ffffff", 
                    inactive="ffffff",
                    urgent_text="1F0036",
                    highlight_method = "block", 
                    urgent_alert_method = "block",
                    this_current_screen_border = "#b53389",
                    this_screen_border = "#b53389",
                    align="left",
                    padding=6,
                    ),
                widget.Spacer(
                    length = 16,
                    align="left",
                    ),
                widget.Sep(
                    foreground="ffffff",
                    align="left",
                    ),
                widget.Spacer(
                    length = 25,
                    align="left",
                    ),
                widget.Clock(
                    fontsize=16,
                    align="left",
                    ),
                widget.Spacer(
                    length = 16,
                    align="left",
                    ),
                widget.Image(
                    filename="/home/alerion/Images/decoration1.png", 
                    margin=3,
                    align="left",
                    ),
                widget.Image(
                   filename="/home/alerion/Images/decoration2.png",
                   margin=5,
                   align="left",
                    ),
                widget.Spacer(
                    length = 20,
                    align="left",
                    ),
                widget.Sep(
                    foreground="ffffff",
                    align="left",
                    ),
                widget.Spacer(
                    length = 10,
                    align="left",
                    ),
                extrawidgets.Visualiser(
                   autostart=True,
                   bar_height=20,
                   bar_colour="#f984ef",
                ),
                widget.Spacer(
                    length = 10,
                    align="left",
                    ),
                widget.Sep(
                foreground="ffffff",
                align="left",
                    ),
                widget.Spacer(
                    length = 10,
                    align="left",
                    ),
                widget.TaskList(    
                    fontsize=14, 
                    foreground="ffffff",
                    highlight_method="block",
                    rounded=True,
                    align="left",
                    border="#8a2be280",
                    icon_size=20,
                    margin=4,
                    padding=5,
                    ),
                widget.Spacer(
                    length = 10,
                    align="left",
                    ),
                widget.Notify(
                    default_timeout=100,
                    align="center"),
                widget.Spacer(
                    align="center",
                    ),
                widget.Spacer(
                    length = 10,
                    align="left",
                    ),
                extrawidgets.Mpris2(
                    foreground="ffffff",
                    stopped_text="Awachimameru kudekunense !",
                    paused_text="C'est en pause !",
                    playing_text="En train d'écouter : " '{track}',
                    scroll_repeat=True,
                    markup=True,
                    align="left",
                    font="sans bold",
                    fontsize=13,
                    border_width=2,
                ),
                widget.Spacer(
                    length = 10,
                    align="left",
                    ),
                widget.Sep(
                    foreground="ffffff",
                    align="left",
                    ),
                widget.Spacer(
                    length = 15,
                    align="left",
                    ),
                 widget.LaunchBar(
                    default_icon="/home/alerion/Images/decoration3.png",
                    icon_size=70,
                    padding=5,
                    progs=[ ('terminal', 'alacritty -e yay -Syyuu', 'Update')],
                ),
                widget.Spacer(
                    length = 15,
                    align="left",
                    ),
                widget.CPU(
                foreground='#ffffff',
                fontsize="14",
                ),
                widget.Memory(
                foreground='#ffffff',
                fontsize="14",
                ),
                widget.Spacer(
                    length = 30,
                    align="left",
                    ),
                widget.Spacer(
                length = 20,
                align="left",
                    ),
                widget.Sep(
                foreground="ffffff",
                align="left",
                    ),
                widget.Spacer(
                    length = 15,
                    align="left",
                    ),
                widget.Systray(
                    icon_size=25,
                    padding=5,
                    ),
                widget.Spacer(
                    length = 15,
                    align="left",
                    ),
                widget.Sep(
                    foreground="ffffff",
                    align="left",
                    ),
                widget.Spacer(
                   length = 20,
                   align="left",
                   ),
                widget.LaunchBar(
                    default_icon="/home/alerion/Images/reboot.png",
                    icon_size=40,
                    padding=5,
                    progs=[('terminal', 'reboot', 'reboot the computer'),],
                ),
                widget.LaunchBar(
                    default_icon="/home/alerion/Images/shutdown.png",
                    icon_size=40,
                    padding=5,
                    progs=[ ('terminal', 'shutdown 0', 'Shutdown the computer')],
                ),
                    widget.Spacer(
                    length = 15,
                    align="left",
                    ),
                    widget.LaunchBar(
                    default_icon="/home/alerion/Images/decoration4.png",
                    icon_size=60,
                    margin=10,
                    progs=[ ('terminal', 'alacritty --hold -e neofetch', 'Update')],
                ),
                widget.Spacer(
                    length = 10,
                    align="left",
                    ),
                
            ],

            # Top bar size + config : 
          
            40,
            margin = [2, 10, 0, 10],
            background="#00000099",
        ),

          # Desktop Wallpaper :

        wallpaper="/home/alerion/Images/animeumbrella.jpg",
        wallpaper_mode = 'fill'
    ),
]



# Drag floating layouts.

mouse = [

    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
    Click([mod], "Button4", lazy.screen.next_group()),
    Click([mod], "Button5", lazy.screen.prev_group()),

]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

# OTHER CONFIG : 

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.

wl_input_rules = None

wmname = "LG3D"

