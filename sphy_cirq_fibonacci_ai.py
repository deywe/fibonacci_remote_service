# ==================================================================================
# 🐦 HARPIA QUANTUM LABS - V18.2 CLOUD AKASHIC (CIRQ INTEGRATED)
# ==================================================================================
import cirq
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sys, time, requests
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

PHI = (1 + np.sqrt(5)) / 2

# ==================================================================================
# MÓDULO I: ORÁCULO CIRQ (VETORIZADO)
# ==================================================================================
def gerar_fluxo_quantico_akashic(t_array):
    resultados = []
    qubit = cirq.LineQubit(0)
    simulator = cirq.Simulator()
    
    for t in t_array:
        circuit = cirq.Circuit(
            cirq.H(qubit),
            cirq.rz(rads=t)(qubit),
            cirq.measure(qubit, key='m')
        )
        result = simulator.simulate(circuit)
        state = result.final_state_vector
        exp_val = np.real(np.conj(state[0]) * state[0] - np.conj(state[1]) * state[1])
        resultados.append(exp_val)
    return np.array(resultados) * 0.03

# ==================================================================================
# MÓDULO II: MOTORES HARPIA (KILL-SWITCH CLOUD)
# ==================================================================================
API_URL = "https://sphyfibonacciapi-cpifhimtglsq6imaebf33f.streamlit.app/"

def VR_Engine_Cloud(p_singular, caos_neg):
    try:
        response = requests.get(API_URL, timeout=5)
        if response.status_code == 200:
            boost_web = 1.25
            status_txt = "🌐 CLOUD SYNC ACTIVE"
            print(f"   [OK] Protocolo SPHY Validado na Nuvem.")
        else:
            sys.exit(f"⚠️ Acesso Negado: Status {response.status_code}")
    except Exception as e:
        sys.exit(f"🚨 ERRO DE CONEXÃO: Motor Akashic Offline. Detalhes: {e}")

    ganho_base = np.exp(-np.abs(p_singular) * 0.01)
    amplificador = (1 + 0.99 * np.tanh(caos_neg))
    return ganho_base * amplificador * (1 + 0.2 * boost_web), status_txt

# ==================================================================================
# MÓDULO III: NÚCLEO AKASHIC
# ==================================================================================
def coerencia_ethereal_vectorized(f_matrix, zeta_base, ruido_local, r_toro_base):
    ruido_filtrado = ruido_local * np.exp(-np.abs(ruido_local) * 1.5)
    peso_memoria = np.where(np.abs(ruido_local) > 0.1, 0.99, 0.95)
    s_coerencia = (peso_memoria * np.exp(-np.abs(ruido_filtrado) * 0.01)) + \
                  ((1 - peso_memoria) * np.exp(-np.abs(ruido_filtrado) * 0.5))
    fase_vibracional = zeta_base + (ruido_filtrado * (1 - s_coerencia) * 0.01)
    distorcao = r_toro_base * (1 + (1 - s_coerencia) * 0.001 * np.sin(f_matrix / PHI))
    return fase_vibracional, distorcao, s_coerencia

def processar_frames_akashic(n_qubits, total_frames, R_TORO, r_TORO, F_ACHAT):
    print(f"⚙️ Iniciando Motor Akashic com backend Cirq...")
    frames = np.arange(total_frames)
    F_grid, Q_grid = np.meshgrid(frames, np.arange(n_qubits), indexing='ij')
    T_grid = F_grid * 0.05
    
    fluxo_t = gerar_fluxo_quantico_akashic(frames * 0.05)
    Fluxo_grid = np.tile(fluxo_t[:, np.newaxis], (1, n_qubits))
    
    Caos_base_grid = (F_grid / total_frames) * 12.0
    P_singular_grid = np.random.uniform(0, 1, size=(total_frames, n_qubits)) * (Caos_base_grid * 0.1)
    
    Ganho_grid, status_msg = VR_Engine_Cloud(P_singular_grid, -Caos_base_grid)
    Zeta_ideal = (PHI * T_grid) + (Q_grid * (2 * np.pi / n_qubits)) + (P_singular_grid - (P_singular_grid * Ganho_grid)) + (Fluxo_grid * 0.05)
    Zeta_real, R_din, S_local = coerencia_ethereal_vectorized(F_grid, Zeta_ideal, (P_singular_grid * 0.05), r_TORO)
    
    X_grid = (R_TORO + R_din * np.cos(T_grid)) * np.cos(Zeta_real)
    Y_grid = (R_TORO + R_din * np.cos(T_grid)) * np.sin(Zeta_real)
    Z_grid = (R_din * F_ACHAT) * np.sin(T_grid)

    data_payload = {'Frame': frames, 'Cloud_Status': [status_msg] * total_frames}
    for i in range(n_qubits):
        data_payload.update({f'q{i}_x': X_grid[:, i], f'q{i}_y': Y_grid[:, i], f'q{i}_z': Z_grid[:, i], f'q{i}_S': S_local[:, i]})

    return pd.DataFrame(data_payload), {"coerencia_media": np.mean(S_local)}

# ==================================================================================
# MÓDULO IV: VISUALIZAÇÃO ETHEREAL (CORRIGIDO)
# ==================================================================================
def visualizar_ethereal(df_sim, n_qubits, stats, R_TORO, r_TORO, F_ACHAT):
    print(f"\n🎨 Renderizando Modo Ethereal...")
    fig = plt.figure(figsize=(14, 10), facecolor='#050505')
    ax = fig.add_subplot(111, projection='3d', facecolor='#050505')
    ax.axis('off')
    ax.set_box_aspect([1, 1, 0.3]) 
    
    # Wireframe do Toro (Background)
    u, v = np.mgrid[0:2*np.pi:100j, 0:2*np.pi:50j]
    x_t = (R_TORO + r_TORO * np.cos(v)) * np.cos(u)
    y_t = (R_TORO + r_TORO * np.cos(v)) * np.sin(u)
    z_t = (r_TORO * F_ACHAT) * np.sin(v)
    ax.plot_wireframe(x_t, y_t, z_t, color='#00FFFF', alpha=0.1, linewidth=0.2)
    
    cores = plt.cm.cool(np.linspace(0, 1, n_qubits))
    lasers = [ax.plot([], [], [], color=cores[i], lw=0.8, alpha=0.6)[0] for i in range(n_qubits)]
    pontos = [ax.plot([], [], [], 'o', color='white', markersize=3, alpha=1.0)[0] for i in range(n_qubits)]
    
    texto_info = ax.text2D(0.02, 0.98, '', transform=ax.transAxes, color='white', fontfamily='monospace')

    def update(frame):
        row = df_sim.iloc[frame % len(df_sim)]
        cloud_status = row['Cloud_Status']
        # Usa o stats passado como argumento para mostrar a fidelidade
        s_medio = stats['coerencia_media'] 

        texto_info.set_text(f"FRAME {frame} | FIDELIDADE: {s_medio:.4%}\nSTATUS: {cloud_status}")
        
        for i in range(n_qubits):
            lookback = max(0, frame - 15)
            # Atualiza trajetórias
            lasers[i].set_data(df_sim[f'q{i}_x'].values[lookback:frame+1], df_sim[f'q{i}_y'].values[lookback:frame+1])
            lasers[i].set_3d_properties(df_sim[f'q{i}_z'].values[lookback:frame+1])
            # Atualiza pontos atuais
            pontos[i].set_data([row[f'q{i}_x']], [row[f'q{i}_y']])
            pontos[i].set_3d_properties([row[f'q{i}_z']])
        
        ax.view_init(elev=30, azim=frame * 0.4)
        return lasers + pontos + [texto_info]
    
    ani = FuncAnimation(fig, update, frames=len(df_sim), interval=20, blit=False)
    plt.show()
# ==================================================================================
# MAIN (CORRIGIDA)
# ==================================================================================
def harpia_main_v18_2():
    print("\n" + "💎"*40 + "\n   ✨ HARPIA V18.2 - ETHEREAL AKASHIC (CIRQ)\n" + "💎"*40)
    try:
        n_qubits = int(input("🔢 Qubits: ") or 120)
        total_frames = int(input("🎞️  Frames: ") or 600)
    except:
        n_qubits, total_frames = 120, 600
    
    df_sim, stats = processar_frames_akashic(n_qubits, total_frames, 21.0, 2.5, 0.000001)
    
    print(f"\n✅ SUCESSO: Coerência Média {stats['coerencia_media']:.6%}")
    
    if input("\n🎨 Abrir Visualizador? (s/n): ").lower() != 'n':
        # AGORA PASSANDO OS 6 ARGUMENTOS CORRETAMENTE (Incluindo 'stats'):
        visualizar_ethereal(df_sim, n_qubits, stats, 21.0, 2.5, 0.000001)

if __name__ == "__main__":
    harpia_main_v18_2()