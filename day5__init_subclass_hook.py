# Modern Python (3.6+) added '__init_subclass__' as a cleaner alternative to metaclasses.
# It lets a base class hook into and inspect child classes whenever they inherit from it.

class PluginRegistry:
    # Central dictionary tracking all active plugins in the system
    registered_plugins = {}

    def __init_subclass__(cls, plugin_name=None, **kwargs):
        super().__init_subclass__(**kwargs)
        
        # Require every subclass to specify a plugin_name
        if not plugin_name:
            raise ValueError(f"Plugin class '{cls.__name__}' must specify a 'plugin_name'!")
        
        # Register the plugin automatically
        cls.registered_plugins[plugin_name] = cls
        print(f"[Registry] Automatically registered plugin: '{plugin_name}' ({cls.__name__})")


# Creating plugins by inheriting from the base class
class AudioPlugin(PluginRegistry, plugin_name="audio_processor"):
    def process(self):
        print("Processing audio signals...")


class ImagePlugin(PluginRegistry, plugin_name="image_filter"):
    def process(self):
        print("Applying image filters...")


#  Example Usage 

print("\n# --- Subclass Hook Demonstration ---")

print("\nActive Plugins registered automatically:")
for name, plugin_cls in PluginRegistry.registered_plugins.items():
    print(f"- {name}: {plugin_cls.__name__}")

# Instantiate and run one of the registered plugins
processor = PluginRegistry.registered_plugins["audio_processor"]()
processor.process()