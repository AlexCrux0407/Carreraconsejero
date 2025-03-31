import psutil
import platform
import socket
import os
import subprocess
from datetime import datetime

try:
    import cpuinfo
    cpu_info_available = True
except ImportError:
    cpu_info_available = False

try:
    import GPUtil
    gpu_available = True
except ImportError:
    gpu_available = False

def get_size(bytes, suffix="B"):
    """
    Escala bytes a su representación legible (KB, MB, GB, TB)
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def get_hardware_info():
    """
    Recopila información detallada sobre el hardware del sistema
    """
    hardware_info = {}
    
    # Información del sistema
    hardware_info['system'] = {}
    hardware_info['system']['platform'] = platform.system()
    hardware_info['system']['release'] = platform.release()
    hardware_info['system']['version'] = platform.version()
    hardware_info['system']['architecture'] = platform.machine()
    hardware_info['system']['hostname'] = socket.gethostname()
    
    # Información de CPU
    hardware_info['cpu'] = {}
    hardware_info['cpu']['processor'] = platform.processor()
    
    if cpu_info_available:
        try:
            cpu_info = cpuinfo.get_cpu_info()
            hardware_info['cpu']['brand'] = cpu_info.get('brand_raw', 'Unknown')
        except Exception:
            hardware_info['cpu']['brand'] = 'Unknown'
    else:
        hardware_info['cpu']['brand'] = platform.processor()
    
    hardware_info['cpu']['cores_physical'] = psutil.cpu_count(logical=False) or 1
    hardware_info['cpu']['cores_total'] = psutil.cpu_count(logical=True) or 1
    
    # Intentar obtener la frecuencia de la CPU
    try:
        cpu_freq = psutil.cpu_freq()
        if cpu_freq:
            hardware_info['cpu']['frequency'] = f"{cpu_freq.current:.2f} MHz"
        else:
            hardware_info['cpu']['frequency'] = "Unknown"
    except Exception:
        hardware_info['cpu']['frequency'] = "Unknown"
    
    # Uso de CPU
    hardware_info['cpu']['usage_percent'] = psutil.cpu_percent(interval=1)
    
    # Información de RAM
    hardware_info['ram'] = {}
    svmem = psutil.virtual_memory()
    hardware_info['ram']['total'] = get_size(svmem.total)
    hardware_info['ram']['total_mb'] = svmem.total / (1024 * 1024)  # Total en MB para cálculos
    hardware_info['ram']['available'] = get_size(svmem.available)
    hardware_info['ram']['used'] = get_size(svmem.used)
    hardware_info['ram']['percentage'] = svmem.percent
    
    # Información de Disco
    hardware_info['disk'] = {}
    partitions = psutil.disk_partitions()
    disk_info = []
    total_disk_size = 0
    
    for partition in partitions:
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
            total_disk_size += partition_usage.total
            disk_info.append({
                'device': partition.device,
                'mountpoint': partition.mountpoint,
                'file_system_type': partition.fstype,
                'total_size': get_size(partition_usage.total),
                'used': get_size(partition_usage.used),
                'free': get_size(partition_usage.free),
                'percentage': partition_usage.percent
            })
        except PermissionError:
            continue
    
    hardware_info['disk']['partitions'] = disk_info
    hardware_info['disk']['total_size'] = get_size(total_disk_size)
    hardware_info['disk']['total_gb'] = total_disk_size / (1024 * 1024 * 1024)  # Total en GB para cálculos
    
    # Información de GPU (si está disponible)
    hardware_info['gpu'] = []
    if gpu_available:
        try:
            gpus = GPUtil.getGPUs()
            for gpu in gpus:
                gpu_info = {
                    'id': gpu.id,
                    'name': gpu.name,
                    'total_memory': f"{gpu.memoryTotal} MB",
                    'free_memory': f"{gpu.memoryFree} MB",
                    'used_memory': f"{gpu.memoryUsed} MB",
                    'temperature': f"{gpu.temperature} °C",
                    'uuid': gpu.uuid
                }
                hardware_info['gpu'].append(gpu_info)
        except Exception as e:
            hardware_info['gpu'].append({'error': str(e)})
    
    # Si no se detectaron GPUs, agregar un valor predeterminado
    if not hardware_info['gpu']:
        hardware_info['gpu'].append({'name': 'No dedicated GPU detected', 'total_memory': '0 MB'})
    
    # Sistema operativo
    hardware_info['os'] = {
        'name': os.name,
        'system': platform.system(),
        'release': platform.release()
    }
    
    return hardware_info