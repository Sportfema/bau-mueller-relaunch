<?php
error_reporting(E_ALL);
ini_set('display_errors', 0);

define('SECRET_KEY', 'mueller2026');
define('DATA_FILE', __DIR__ . '/votes_data.json');

header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit;
}

function load_votes_data() {
    if (!file_exists(DATA_FILE)) {
        return array(
            'total' => 0,
            'counts' => array('super' => 0, 'gut' => 0, 'feedback' => 0),
            'votes' => array()
        );
    }
    $content = @file_get_contents(DATA_FILE);
    $data = json_decode($content, true);
    if (!is_array($data)) {
        return array(
            'total' => 0,
            'counts' => array('super' => 0, 'gut' => 0, 'feedback' => 0),
            'votes' => array()
        );
    }
    return $data;
}

function save_votes_data($data) {
    @file_put_contents(DATA_FILE, json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE), LOCK_EX);
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    header('Content-Type: application/json; charset=utf-8');
    $raw = file_get_contents('php://input');
    $payload = json_decode($raw, true);
    
    if (!$payload || empty($payload['vote'])) {
        http_response_code(400);
        echo json_encode(array('success' => false, 'error' => 'Keine Stimme übergeben'));
        exit;
    }
    
    $voteType = in_array($payload['vote'], array('super', 'gut', 'feedback')) ? $payload['vote'] : 'feedback';
    $page = isset($payload['url']) ? htmlspecialchars(substr($payload['url'], 0, 200)) : '/';
    $comment = isset($payload['comment']) ? htmlspecialchars(substr($payload['comment'], 0, 500)) : '';
    $timestamp = date('Y-m-d H:i:s');
    
    $data = load_votes_data();
    $data['total']++;
    if (!isset($data['counts'][$voteType])) {
        $data['counts'][$voteType] = 0;
    }
    $data['counts'][$voteType]++;
    
    array_unshift($data['votes'], array(
        'timestamp' => $timestamp,
        'vote' => $voteType,
        'page' => $page,
        'comment' => $comment
    ));
    if (count($data['votes']) > 100) {
        $data['votes'] = array_slice($data['votes'], 0, 100);
    }
    
    save_votes_data($data);
    
    echo json_encode(array(
        'success' => true,
        'message' => 'Stimme erfolgreich erfasst.',
        'tally' => $data['counts']
    ));
    exit;
}

$providedKey = isset($_GET['key']) ? $_GET['key'] : '';
if ($providedKey !== SECRET_KEY) {
    http_response_code(403);
    echo '<!DOCTYPE html><html lang="de"><head><meta charset="utf-8"><title>Zugriff geschützt</title>';
    echo '<style>body{font-family:sans-serif;text-align:center;padding:50px;background:#f5f4f0;color:#333;}</style></head>';
    echo '<body><h2>Zugriff geschützt</h2><p>Bitte nutzen Sie den autorisierten Link: <code>?key=mueller2026</code></p></body></html>';
    exit;
}

$data = load_votes_data();
$total = $data['total'];
$super = isset($data['counts']['super']) ? $data['counts']['super'] : 0;
$gut = isset($data['counts']['gut']) ? $data['counts']['gut'] : 0;
$feedback = isset($data['counts']['feedback']) ? $data['counts']['feedback'] : 0;

$pSuper = $total > 0 ? round(($super / $total) * 100) : 0;
$pGut = $total > 0 ? round(($gut / $total) * 100) : 0;
$pFeedback = $total > 0 ? round(($feedback / $total) * 100) : 0;

if (isset($_GET['format']) && $_GET['format'] === 'json') {
    header('Content-Type: application/json; charset=utf-8');
    echo json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
    exit;
}
?>
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Website-Voting Auswertung · Arthur Müller Relaunch</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@700;800&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #F8F5EE;
      --card-bg: #FFFFFF;
      --charcoal: #1C1B1A;
      --red: #E31936;
      --text: #2B2825;
      --muted: #7A746B;
      --border: rgba(28, 27, 26, 0.1);
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.5;
      padding: 32px 16px;
    }
    .container { max-width: 980px; margin: 0 auto; }
    header {
      background: var(--charcoal);
      color: #fff;
      padding: 32px 28px;
      border-radius: 24px;
      margin-bottom: 24px;
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
      box-shadow: 0 10px 25px rgba(0,0,0,0.08);
    }
    h1 {
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 1.5rem;
      font-weight: 800;
      letter-spacing: -0.02em;
    }
    .badge {
      display: inline-block;
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      color: var(--red);
      font-weight: 700;
      margin-bottom: 4px;
    }
    .total-badge {
      background: rgba(255,255,255,0.1);
      padding: 12px 20px;
      border-radius: 16px;
      text-align: right;
    }
    .total-number {
      font-size: 2.2rem;
      font-weight: 800;
      color: #fff;
      font-family: 'Plus Jakarta Sans', sans-serif;
      line-height: 1;
    }
    .total-label {
      font-size: 0.75rem;
      color: #A39E93;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 16px;
      margin-bottom: 24px;
    }
    .stat-card {
      background: var(--card-bg);
      padding: 24px;
      border-radius: 20px;
      border: 1px solid var(--border);
      box-shadow: 0 4px 15px rgba(0,0,0,0.03);
    }
    .stat-card.super { border-top: 4px solid #10B981; }
    .stat-card.gut { border-top: 4px solid #3B82F6; }
    .stat-card.feedback { border-top: 4px solid #F59E0B; }
    .stat-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
    }
    .stat-title { font-weight: 600; font-size: 0.95rem; }
    .stat-emoji { font-size: 1.8rem; }
    .stat-count {
      font-size: 2.2rem;
      font-weight: 800;
      font-family: 'Plus Jakarta Sans', sans-serif;
      color: var(--charcoal);
      line-height: 1;
      margin-bottom: 4px;
    }
    .stat-pct { font-size: 0.85rem; color: var(--muted); font-weight: 500; }
    .progress-bar-wrap {
      background: var(--card-bg);
      padding: 24px;
      border-radius: 20px;
      border: 1px solid var(--border);
      margin-bottom: 24px;
    }
    .progress-bar-title {
      font-weight: 700;
      font-size: 1rem;
      margin-bottom: 14px;
      font-family: 'Plus Jakarta Sans', sans-serif;
    }
    .bar-container {
      height: 20px;
      border-radius: 10px;
      background: #E5E0D5;
      overflow: hidden;
      display: flex;
    }
    .bar-super { background: #10B981; width: <?php echo $pSuper; ?>%; }
    .bar-gut { background: #3B82F6; width: <?php echo $pGut; ?>%; }
    .bar-feedback { background: #F59E0B; width: <?php echo $pFeedback; ?>%; }
    .bar-legend {
      display: flex;
      flex-wrap: wrap;
      gap: 16px;
      margin-top: 14px;
      font-size: 0.85rem;
    }
    .legend-item { display: flex; align-items: center; gap: 6px; }
    .dot { width: 10px; height: 10px; border-radius: 50%; display: inline-block; }
    .dot.super { background: #10B981; }
    .dot.gut { background: #3B82F6; }
    .dot.feedback { background: #F59E0B; }
    .history-wrap {
      background: var(--card-bg);
      padding: 24px;
      border-radius: 20px;
      border: 1px solid var(--border);
    }
    .history-title {
      font-weight: 700;
      font-size: 1.1rem;
      margin-bottom: 16px;
      font-family: 'Plus Jakarta Sans', sans-serif;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    table { width: 100%; border-collapse: collapse; font-size: 0.875rem; }
    th {
      text-align: left;
      padding: 10px 12px;
      background: #F8F5EE;
      color: var(--muted);
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      border-radius: 8px;
    }
    td { padding: 12px; border-bottom: 1px solid var(--border); }
    tr:last-child td { border-bottom: none; }
    .vote-pill {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 4px 10px;
      border-radius: 12px;
      font-weight: 600;
      font-size: 0.8rem;
    }
    .vote-pill.super { background: rgba(16,185,129,0.12); color: #059669; }
    .vote-pill.gut { background: rgba(59,130,246,0.12); color: #2563EB; }
    .vote-pill.feedback { background: rgba(245,158,11,0.12); color: #D97706; }
    .refresh-btn {
      background: var(--charcoal);
      color: #fff;
      text-decoration: none;
      font-size: 0.8rem;
      font-weight: 600;
      padding: 8px 14px;
      border-radius: 10px;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: background 0.2s;
    }
    .refresh-btn:hover { background: #333; }
  </style>
</head>
<body>
  <div class="container">
    <header>
      <div>
        <span class="badge">Live-Auswertung</span>
        <h1>Website-Voting · Neues Design</h1>
        <p style="color: #A39E93; font-size: 0.85rem; margin-top: 4px;">
          Arthur Müller e.K. · Colditz · Relaunch 2026
        </p>
      </div>
      <div class="total-badge">
        <div class="total-number"><?php echo $total; ?></div>
        <div class="total-label">Stimmen Gesamt</div>
      </div>
    </header>

    <div class="grid">
      <div class="stat-card super">
        <div class="stat-header">
          <span class="stat-title">Begeistert</span>
          <span class="stat-emoji">😍</span>
        </div>
        <div class="stat-count"><?php echo $super; ?></div>
        <div class="stat-pct"><?php echo $pSuper; ?>% aller Teilnehmer</div>
      </div>

      <div class="stat-card gut">
        <div class="stat-header">
          <span class="stat-title">Sehr gut</span>
          <span class="stat-emoji">👍</span>
        </div>
        <div class="stat-count"><?php echo $gut; ?></div>
        <div class="stat-pct"><?php echo $pGut; ?>% aller Teilnehmer</div>
      </div>

      <div class="stat-card feedback">
        <div class="stat-header">
          <span class="stat-title">Geht so / Feedback</span>
          <span class="stat-emoji">💬</span>
        </div>
        <div class="stat-count"><?php echo $feedback; ?></div>
        <div class="stat-pct"><?php echo $pFeedback; ?>% aller Teilnehmer</div>
      </div>
    </div>

    <div class="progress-bar-wrap">
      <div class="progress-bar-title">Stimmungsverteilung</div>
      <div class="bar-container">
        <div class="bar-super" title="Begeistert: <?php echo $pSuper; ?>%"></div>
        <div class="bar-gut" title="Sehr gut: <?php echo $pGut; ?>%"></div>
        <div class="bar-feedback" title="Feedback: <?php echo $pFeedback; ?>%"></div>
      </div>
      <div class="bar-legend">
        <div class="legend-item"><span class="dot super"></span> Begeistert (<?php echo $pSuper; ?>%)</div>
        <div class="legend-item"><span class="dot gut"></span> Sehr gut (<?php echo $pGut; ?>%)</div>
        <div class="legend-item"><span class="dot feedback"></span> Geht so (<?php echo $pFeedback; ?>%)</div>
      </div>
    </div>

    <div class="history-wrap">
      <div class="history-title">
        <span>Letzte Stimmen</span>
        <a href="?key=<?php echo urlencode(SECRET_KEY); ?>" class="refresh-btn">
          ↻ Aktualisieren
        </a>
      </div>
      
      <?php if (empty($data['votes'])): ?>
        <p style="color: var(--muted); font-size: 0.9rem; padding: 20px 0; text-align: center;">
          Noch keine Stimmen erfasst. Sobald Besucher im Popup abstimmen, erscheinen die Einträge hier in Echtzeit.
        </p>
      <?php else: ?>
        <div style="overflow-x: auto;">
          <table>
            <thead>
              <tr>
                <th>Zeitpunkt</th>
                <th>Bewertung</th>
                <th>Aufgerufene Seite</th>
                <th>Anmerkung</th>
              </tr>
            </thead>
            <tbody>
              <?php foreach (array_slice($data['votes'], 0, 30) as $row): ?>
                <tr>
                  <td style="white-space: nowrap; font-size: 0.8rem; color: var(--muted);">
                    <?php echo date('d.m.Y H:i', strtotime($row['timestamp'])); ?> Uhr
                  </td>
                  <td>
                    <?php if ($row['vote'] === 'super'): ?>
                      <span class="vote-pill super">😍 Begeistert</span>
                    <?php elseif ($row['vote'] === 'gut'): ?>
                      <span class="vote-pill gut">👍 Sehr gut</span>
                    <?php else: ?>
                      <span class="vote-pill feedback">💬 Geht so</span>
                    <?php endif; ?>
                  </td>
                  <td style="font-family: monospace; font-size: 0.8rem;">
                    <?php echo htmlspecialchars($row['page']); ?>
                  </td>
                  <td style="color: var(--muted); font-style: italic;">
                    <?php echo !empty($row['comment']) ? htmlspecialchars($row['comment']) : '–'; ?>
                  </td>
                </tr>
              <?php endforeach; ?>
            </tbody>
          </table>
        </div>
      <?php endif; ?>
    </div>

    <div style="text-align: center; margin-top: 30px; font-size: 0.75rem; color: var(--muted);">
      Zimmerei & Baugeschäft Arthur Müller e.K. · Geithainer Str. 32 · 04680 Colditz · Inhaber: Dipl.-Ing. Tobias Müller
    </div>

  </div>
</body>
</html>